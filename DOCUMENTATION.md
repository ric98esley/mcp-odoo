# Documentación MCP-Odoo Mejorado

## Introducción

Este documento describe las mejoras implementadas en el MCP (Model Context Protocol) para Odoo, que amplía significativamente las capacidades del repositorio original añadiendo nuevas herramientas, recursos y prompts para las áreas de ventas, compras, inventario y contabilidad.

El objetivo de estas mejoras es proporcionar una integración más completa y funcional entre Odoo ERP y los modelos de lenguaje como Claude, permitiendo interacciones más ricas y útiles en contextos empresariales.

## Arquitectura

La arquitectura del MCP-Odoo mejorado sigue un diseño modular que facilita la extensión y el mantenimiento:

```
mcp-odoo/
├── src/
│   └── odoo_mcp/
│       ├── __init__.py           # Inicialización del paquete
│       ├── server.py             # Servidor MCP principal
│       ├── odoo_client.py        # Cliente para conexión con Odoo
│       ├── models.py             # Modelos Pydantic para validación
│       ├── extensions.py         # Registro centralizado de extensiones
│       ├── prompts.py            # Prompts para análisis y asistencia
│       ├── resources.py          # Recursos MCP (URIs)
│       ├── tools_sales.py        # Herramientas para ventas
│       ├── tools_purchase.py     # Herramientas para compras
│       ├── tools_inventory.py    # Herramientas para inventario
│       └── tools_accounting.py   # Herramientas para contabilidad
├── pyproject.toml               # Configuración del paquete
├── Dockerfile                   # Configuración para Docker
└── validation.py               # Script de validación
```

## Nuevas Funcionalidades

### 1. Herramientas (Tools)

Las herramientas permiten a los modelos de lenguaje realizar acciones específicas en Odoo:

#### Ventas
- `search_sales_orders`: Busca órdenes de venta con filtros avanzados
- `create_sales_order`: Crea una nueva orden de venta
- `analyze_sales_performance`: Analiza el rendimiento de ventas por período, producto o cliente
- `get_customer_insights`: Obtiene información detallada sobre un cliente específico

#### Compras
- `search_purchase_orders`: Busca órdenes de compra con filtros avanzados
- `create_purchase_order`: Crea una nueva orden de compra
- `analyze_supplier_performance`: Analiza el rendimiento de proveedores

#### Inventario
- `check_product_availability`: Verifica la disponibilidad de stock para productos
- `create_inventory_adjustment`: Crea un ajuste de inventario
- `analyze_inventory_turnover`: Calcula y analiza la rotación de inventario

#### Contabilidad
- `search_journal_entries`: Busca asientos contables con filtros
- `create_journal_entry`: Crea un nuevo asiento contable
- `analyze_financial_ratios`: Calcula ratios financieros clave

### 2. Recursos (Resources)

Los recursos proporcionan acceso a datos de Odoo mediante URIs:

#### Ventas
- `odoo://sales/orders`: Lista órdenes de venta
- `odoo://sales/order/{order_id}`: Obtiene detalles de una orden específica
- `odoo://sales/products`: Lista productos vendibles
- `odoo://sales/customers`: Lista clientes

#### Compras
- `odoo://purchase/orders`: Lista órdenes de compra
- `odoo://purchase/order/{order_id}`: Obtiene detalles de una orden específica
- `odoo://purchase/suppliers`: Lista proveedores

#### Inventario
- `odoo://inventory/products`: Lista productos en inventario
- `odoo://inventory/stock/{location_id}`: Obtiene niveles de stock en una ubicación
- `odoo://inventory/movements`: Lista movimientos de inventario

#### Contabilidad
- `odoo://accounting/accounts`: Lista cuentas contables
- `odoo://accounting/journal_entries`: Lista asientos contables
- `odoo://accounting/reports/{report_type}`: Obtiene informes financieros

### 3. Prompts

Se han añadido prompts especializados para diferentes áreas:

- **Análisis de ventas**: Prompts para analizar tendencias, rendimiento y oportunidades
- **Gestión de inventario**: Prompts para optimización de stock y planificación
- **Planificación de recursos humanos**: Prompts para gestión de personal y horarios
- **Análisis financiero**: Prompts para interpretación de datos contables y financieros

## Guía de Uso

### Instalación

#### Opción 1: Usando el paquete de Python

```bash
# Clonar el repositorio
git clone https://github.com/tuanle96/mcp-odoo.git
cd mcp-odoo

# Instalar el paquete
pip install -e .

# Ejecutar como módulo
python -m src.odoo_mcp
```

#### Opción 2: Usando Docker

```bash
# Construir la imagen
docker build -t mcp/odoo:latest -f Dockerfile .

# Ejecutar el contenedor
docker run -i --rm \
  -e ODOO_URL=https://tu-instancia-odoo.com \
  -e ODOO_DB=nombre-de-tu-base-de-datos \
  -e ODOO_USERNAME=tu-usuario \
  -e ODOO_PASSWORD=tu-contraseña \
  mcp/odoo
```

### Configuración

El MCP-Odoo puede configurarse mediante variables de entorno o un archivo de configuración:

#### Variables de entorno

```bash
export ODOO_URL=https://tu-instancia-odoo.com
export ODOO_DB=nombre-de-tu-base-de-datos
export ODOO_USERNAME=tu-usuario
export ODOO_PASSWORD=tu-contraseña
```

#### Archivo de configuración

Crear un archivo `odoo_config.json` en el directorio de trabajo:

```json
{
  "url": "https://tu-instancia-odoo.com",
  "db": "nombre-de-tu-base-de-datos",
  "username": "tu-usuario",
  "password": "tu-contraseña"
}
```

### Integración con Claude Desktop

Para usar el MCP-Odoo con Claude Desktop, añade la siguiente configuración a tu `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "odoo": {
      "command": "python",
      "args": ["-m", "src.odoo_mcp"],
      "env": {
        "ODOO_URL": "https://tu-instancia-odoo.com",
        "ODOO_DB": "nombre-de-tu-base-de-datos",
        "ODOO_USERNAME": "tu-usuario",
        "ODOO_PASSWORD": "tu-contraseña"
      }
    }
  }
}
```

Para usar la versión Docker:

```json
{
  "mcpServers": {
    "odoo": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e", "ODOO_URL",
        "-e", "ODOO_DB",
        "-e", "ODOO_USERNAME",
        "-e", "ODOO_PASSWORD",
        "mcp/odoo"
      ],
      "env": {
        "ODOO_URL": "https://tu-instancia-odoo.com",
        "ODOO_DB": "nombre-de-tu-base-de-datos",
        "ODOO_USERNAME": "tu-usuario",
        "ODOO_PASSWORD": "tu-contraseña"
      }
    }
  }
}
```

## Ejemplos de Uso

### Ejemplo 1: Análisis de ventas

```
Usando el MCP de Odoo, analiza las ventas del último trimestre y muestra los productos más vendidos.
```

### Ejemplo 2: Verificación de inventario

```
Verifica la disponibilidad de stock para los productos X, Y y Z en el almacén principal.
```

### Ejemplo 3: Análisis financiero

```
Calcula los ratios de liquidez y rentabilidad para el año fiscal actual y compáralos con el año anterior.
```

### Ejemplo 4: Creación de órdenes de compra

```
Crea una orden de compra para el proveedor ABC con los siguientes productos: 10 unidades del producto X y 5 unidades del producto Y.
```

## Extensión del Sistema

El sistema está diseñado para ser fácilmente extensible. Para añadir nuevas funcionalidades:

1. **Nuevas herramientas**: Crea un nuevo archivo `tools_*.py` siguiendo el patrón existente
2. **Nuevos recursos**: Añade nuevos recursos en `resources.py`
3. **Nuevos prompts**: Añade nuevos prompts en `prompts.py`
4. **Registro de extensiones**: Actualiza `extensions.py` para registrar las nuevas funcionalidades

## Solución de Problemas

### Problemas de conexión

Si experimentas problemas de conexión con Odoo:

1. Verifica las credenciales en las variables de entorno o archivo de configuración
2. Asegúrate de que la URL de Odoo es accesible desde donde ejecutas el MCP
3. Verifica que el usuario tiene permisos suficientes en Odoo

### Errores en las herramientas

Si una herramienta devuelve un error:

1. Revisa los parámetros proporcionados
2. Verifica que los IDs de registros existen en Odoo
3. Comprueba los permisos del usuario para la operación específica

## Validación

Se incluye un script de validación (`validation.py`) que puede ejecutarse para verificar que todas las funcionalidades están correctamente implementadas y son compatibles con tu instancia de Odoo:

```bash
python validation.py
```

## Contribución

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un fork del repositorio
2. Crea una rama para tu funcionalidad (`git checkout -b feature/nueva-funcionalidad`)
3. Realiza tus cambios y añade pruebas
4. Envía un pull request

## Licencia

Este proyecto se distribuye bajo la misma licencia que el repositorio original.
