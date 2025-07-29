"""
Implementación de modelos Pydantic para MCP-Odoo
"""

from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel, Field

# ----- Pydantic models for type safety -----

class DomainCondition(BaseModel):
    """A single condition in a search domain"""

    field: str = Field(description="Field name to search")
    operator: str = Field(
        description="Operator (e.g., '=', '!=', '>', '<', 'in', 'not in', 'like', 'ilike')"
    )
    value: Any = Field(description="Value to compare against")

    def to_tuple(self) -> List:
        """Convert to Odoo domain condition tuple"""
        return [self.field, self.operator, self.value]


class SearchDomain(BaseModel):
    """Search domain for Odoo models"""

    conditions: List[DomainCondition] = Field(
        default_factory=list,
        description="List of conditions for searching. All conditions are combined with AND operator.",
    )

    def to_domain_list(self) -> List[List]:
        """Convert to Odoo domain list format"""
        return [condition.to_tuple() for condition in self.conditions]


class EmployeeSearchResult(BaseModel):
    """Represents a single employee search result."""

    id: int = Field(description="Employee ID")
    name: str = Field(description="Employee name")


class SearchEmployeeResponse(BaseModel):
    """Response model for the search_employee tool."""

    success: bool = Field(description="Indicates if the search was successful")
    result: Optional[List[EmployeeSearchResult]] = Field(
        default=None, description="List of employee search results"
    )
    error: Optional[str] = Field(default=None, description="Error message, if any")


class Holiday(BaseModel):
    """Represents a single holiday."""

    display_name: str = Field(description="Display name of the holiday")
    start_datetime: str = Field(description="Start date and time of the holiday")
    stop_datetime: str = Field(description="End date and time of the holiday")
    employee_id: List[Union[int, str]] = Field(
        description="Employee ID associated with the holiday"
    )
    name: str = Field(description="Name of the holiday")
    state: str = Field(description="State of the holiday")


class SearchHolidaysResponse(BaseModel):
    """Response model for the search_holidays tool."""

    success: bool = Field(description="Indicates if the search was successful")
    result: Optional[List[Holiday]] = Field(
        default=None, description="List of holidays found"
    )
    error: Optional[str] = Field(default=None, description="Error message, if any")



# Modelos para Ventas
class SalesOrderLineCreate(BaseModel):
    """Línea de pedido de venta para creación"""
    product_id: int = Field(description="ID del producto")
    product_uom_qty: float = Field(description="Cantidad")
    price_unit: Optional[float] = Field(None, description="Precio unitario (opcional, Odoo puede calcularlo)")

class SalesOrderCreate(BaseModel):
    """Datos para crear un pedido de venta"""
    partner_id: int = Field(description="ID del cliente")
    order_lines: List[SalesOrderLineCreate] = Field(description="Líneas del pedido")
    date_order: Optional[str] = Field(None, description="Fecha del pedido (YYYY-MM-DD)")

class SalesOrderFilter(BaseModel):
    """Filtros para búsqueda de pedidos de venta"""
    partner_id: Optional[int] = Field(None, description="Filtrar por cliente ID")
    date_from: Optional[str] = Field(None, description="Fecha inicial (YYYY-MM-DD)")
    date_to: Optional[str] = Field(None, description="Fecha final (YYYY-MM-DD)")
    state: Optional[str] = Field(None, description="Estado del pedido (e.g., 'sale', 'draft', 'done')")
    limit: Optional[int] = Field(20, description="Límite de resultados")
    offset: Optional[int] = Field(0, description="Offset para paginación")
    order: Optional[str] = Field(None, description="Criterio de ordenación (e.g., 'date_order DESC')")

class SalesPerformanceInput(BaseModel):
    """Parámetros para análisis de rendimiento de ventas"""
    date_from: str = Field(description="Fecha inicial (YYYY-MM-DD)")
    date_to: str = Field(description="Fecha final (YYYY-MM-DD)")
    group_by: Optional[str] = Field(None, description="Agrupar por ('product', 'customer', 'salesperson')")

# Modelos para Compras
class PurchaseOrderLineCreate(BaseModel):
    """Línea de orden de compra para creación"""
    product_id: int = Field(description="ID del producto")
    product_qty: float = Field(description="Cantidad")
    price_unit: Optional[float] = Field(None, description="Precio unitario (opcional)")

class PurchaseOrderCreate(BaseModel):
    """Datos para crear una orden de compra"""
    partner_id: int = Field(description="ID del proveedor")
    order_lines: List[PurchaseOrderLineCreate] = Field(description="Líneas de la orden")
    date_order: Optional[str] = Field(None, description="Fecha de la orden (YYYY-MM-DD)")

class PurchaseOrderFilter(BaseModel):
    """Filtros para búsqueda de órdenes de compra"""
    partner_id: Optional[int] = Field(None, description="Filtrar por proveedor ID")
    date_from: Optional[str] = Field(None, description="Fecha inicial (YYYY-MM-DD)")
    date_to: Optional[str] = Field(None, description="Fecha final (YYYY-MM-DD)")
    state: Optional[str] = Field(None, description="Estado de la orden (e.g., 'purchase', 'draft', 'done')")
    limit: Optional[int] = Field(20, description="Límite de resultados")
    offset: Optional[int] = Field(0, description="Offset para paginación")
    order: Optional[str] = Field(None, description="Criterio de ordenación (e.g., 'date_order DESC')")

class SupplierPerformanceInput(BaseModel):
    """Parámetros para análisis de rendimiento de proveedores"""
    date_from: str = Field(description="Fecha inicial (YYYY-MM-DD)")
    date_to: str = Field(description="Fecha final (YYYY-MM-DD)")
    supplier_ids: Optional[List[int]] = Field(None, description="Lista de IDs de proveedores (opcional)")

# Modelos para Inventario
class ProductAvailabilityInput(BaseModel):
    """Parámetros para verificar disponibilidad de productos"""
    product_ids: List[int] = Field(description="Lista de IDs de productos")
    location_id: Optional[int] = Field(None, description="ID de la ubicación específica (opcional)")

class InventoryLineAdjustment(BaseModel):
    """Línea de ajuste de inventario"""
    product_id: int = Field(description="ID del producto")
    location_id: int = Field(description="ID de la ubicación")
    product_qty: float = Field(description="Cantidad contada real")

class InventoryAdjustmentCreate(BaseModel):
    """Datos para crear un ajuste de inventario"""
    name: str = Field(description="Nombre o descripción del ajuste")
    adjustment_lines: List[InventoryLineAdjustment] = Field(description="Líneas de ajuste")
    date: Optional[str] = Field(None, description="Fecha del ajuste (YYYY-MM-DD)")

class InventoryTurnoverInput(BaseModel):
    """Parámetros para análisis de rotación de inventario"""
    date_from: str = Field(description="Fecha inicial (YYYY-MM-DD)")
    date_to: str = Field(description="Fecha final (YYYY-MM-DD)")
    product_ids: Optional[List[int]] = Field(None, description="Lista de IDs de productos (opcional)")
    category_id: Optional[int] = Field(None, description="ID de categoría de producto (opcional)")

# Modelos para Contabilidad
class JournalEntryLineCreate(BaseModel):
    """Línea de asiento contable para creación"""
    account_id: int = Field(description="ID de la cuenta contable")
    partner_id: Optional[int] = Field(None, description="ID del partner (opcional)")
    name: Optional[str] = Field(None, description="Descripción de la línea")
    debit: float = Field(0.0, description="Importe al debe")
    credit: float = Field(0.0, description="Importe al haber")

class JournalEntryCreate(BaseModel):
    """Datos para crear un asiento contable"""
    ref: Optional[str] = Field(None, description="Referencia del asiento")
    journal_id: int = Field(description="ID del diario contable")
    date: Optional[str] = Field(None, description="Fecha del asiento (YYYY-MM-DD)")
    lines: List[JournalEntryLineCreate] = Field(description="Líneas del asiento (debe y haber deben cuadrar)")

class JournalEntryFilter(BaseModel):
    """Filtros para búsqueda de asientos contables"""
    date_from: Optional[str] = Field(None, description="Fecha inicial (YYYY-MM-DD)")
    date_to: Optional[str] = Field(None, description="Fecha final (YYYY-MM-DD)")
    journal_id: Optional[int] = Field(None, description="Filtrar por diario contable ID")
    state: Optional[str] = Field(None, description="Estado del asiento (e.g., 'posted', 'draft')")
    limit: Optional[int] = Field(20, description="Límite de resultados")
    offset: Optional[int] = Field(0, description="Offset para paginación")

class FinancialRatioInput(BaseModel):
    """Parámetros para cálculo de ratios financieros"""
    date_from: str = Field(description="Fecha inicial (YYYY-MM-DD)")
    date_to: str = Field(description="Fecha final (YYYY-MM-DD)")
    ratios: List[str] = Field(description="Lista de ratios a calcular (e.g., ['liquidity', 'profitability', 'debt'])")
