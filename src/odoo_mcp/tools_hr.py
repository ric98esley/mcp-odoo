"""
Implement original tools for hr Create by tuanle96
"""

from typing import Dict, List, Any, Optional
from datetime import datetime, timedelta
from mcp.server.fastmcp import FastMCP, Context

from .models import (
    SearchEmployeeResponse,
    SearchHolidaysResponse,
    EmployeeSearchResult,
    Holiday
)

def register_hr_tools(mcp: FastMCP) -> None:
    @mcp.tool(description="Search for employees by name")
    def search_employee(
        ctx: Context,
        name: str,
        limit: int = 20,
    ) -> SearchEmployeeResponse:
        """
        Search for employees by name using Odoo's name_search method.

        Parameters:
            name: The name (or part of the name) to search for.
            limit: The maximum number of results to return (default 20).

        Returns:
            SearchEmployeeResponse containing results or error information.
        """
        odoo = ctx.request_context.lifespan_context.odoo
        model = "hr.employee"
        method = "name_search"

        args = []
        kwargs = {"name": name, "limit": limit}

        try:
            result = odoo.execute_method(model, method, *args, **kwargs)
            parsed_result = [
                EmployeeSearchResult(id=item[0], name=item[1]) for item in result
            ]
            return SearchEmployeeResponse(success=True, result=parsed_result)
        except Exception as e:
            return SearchEmployeeResponse(success=False, error=str(e))


    @mcp.tool(description="Search for holidays within a date range")
    def search_holidays(
        ctx: Context,
        start_date: str,
        end_date: str,
        employee_id: Optional[int] = None,
    ) -> SearchHolidaysResponse:
        """
        Searches for holidays within a specified date range.

        Parameters:
            start_date: Start date in YYYY-MM-DD format.
            end_date: End date in YYYY-MM-DD format.
            employee_id: Optional employee ID to filter holidays.

        Returns:
            SearchHolidaysResponse:  Object containing the search results.
        """
        odoo = ctx.request_context.lifespan_context.odoo

        # Validate date format using datetime
        try:
            datetime.strptime(start_date, "%Y-%m-%d")
        except ValueError:
            return SearchHolidaysResponse(
                success=False, error="Invalid start_date format. Use YYYY-MM-DD."
            )
        try:
            datetime.strptime(end_date, "%Y-%m-%d")
        except ValueError:
            return SearchHolidaysResponse(
                success=False, error="Invalid end_date format. Use YYYY-MM-DD."
            )

        # Calculate adjusted start_date (subtract one day)
        start_date_dt = datetime.strptime(start_date, "%Y-%m-%d")
        adjusted_start_date_dt = start_date_dt - timedelta(days=1)
        adjusted_start_date = adjusted_start_date_dt.strftime("%Y-%m-%d")

        # Build the domain
        domain = [
            "&",
            ["start_datetime", "<=", f"{end_date} 22:59:59"],
            # Use adjusted date
            ["stop_datetime", ">=", f"{adjusted_start_date} 23:00:00"],
        ]
        if employee_id:
            domain.append(
                ["employee_id", "=", employee_id],
            )

        try:
            holidays = odoo.search_read(
                model_name="hr.leave.report.calendar",
                domain=domain,
            )
            parsed_holidays = [Holiday(**holiday) for holiday in holidays]
            return SearchHolidaysResponse(success=True, result=parsed_holidays)

        except Exception as e:
            return SearchHolidaysResponse(success=False, error=str(e))
