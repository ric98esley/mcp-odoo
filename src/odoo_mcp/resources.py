"""
Integration of resources for MCP-Odoo
"""
import json

from mcp.server.fastmcp import FastMCP
from odoo_mcp.odoo_client import get_odoo_client


def register_all_resources(mcp: FastMCP) -> None:
    """Registra todos los recursos disponibles"""
    # ----- MCP Resources -----
    @mcp.resource(
        "odoo://models", description="List all available models in the Odoo system"
    )
    def get_models() -> str:
        """Lists all available models in the Odoo system"""
        odoo_client = get_odoo_client()
        models = odoo_client.get_models()
        return json.dumps(models, indent=2)


    @mcp.resource(
        "odoo://model/{model_name}",
        description="Get detailed information about a specific model including fields",
    )
    def get_model_info(model_name: str) -> str:
        """
        Get information about a specific model

        Parameters:
            model_name: Name of the Odoo model (e.g., 'res.partner')
        """
        odoo_client = get_odoo_client()
        try:
            # Get model info
            model_info = odoo_client.get_model_info(model_name)

            # Get field definitions
            fields = odoo_client.get_model_fields(model_name)
            model_info["fields"] = fields

            return json.dumps(model_info, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)


    @mcp.resource(
        "odoo://record/{model_name}/{record_id}",
        description="Get detailed information of a specific record by ID",
    )
    def get_record(model_name: str, record_id: str) -> str:
        """
        Get a specific record by ID

        Parameters:
            model_name: Name of the Odoo model (e.g., 'res.partner')
            record_id: ID of the record
        """
        odoo_client = get_odoo_client()
        try:
            record_id_int = int(record_id)
            record = odoo_client.read_records(model_name, [record_id_int])
            if not record:
                return json.dumps(
                    {"error": f"Record not found: {model_name} ID {record_id}"}, indent=2
                )
            return json.dumps(record[0], indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)


    @mcp.resource(
        "odoo://search/{model_name}/{domain}",
        description="Search for records matching the domain",
    )
    def search_records_resource(model_name: str, domain: str) -> str:
        """
        Search for records that match a domain

        Parameters:
            model_name: Name of the Odoo model (e.g., 'res.partner')
            domain: Search domain in JSON format (e.g., '[["name", "ilike", "test"]]')
        """
        odoo_client = get_odoo_client()
        try:
            # Parse domain from JSON string
            domain_list = json.loads(domain)

            # Set a reasonable default limit
            limit = 10

            # Perform search_read for efficiency
            results = odoo_client.search_read(model_name, domain_list, limit=limit)

            return json.dumps(results, indent=2)
        except Exception as e:
            return json.dumps({"error": str(e)}, indent=2)
