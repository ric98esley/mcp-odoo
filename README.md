<<<<<<< HEAD
# Odoo MCP Server

An MCP server implementation that integrates with Odoo ERP systems, enabling AI assistants to interact with Odoo data and functionality through the Model Context Protocol.

## Features

* **Comprehensive Odoo Integration**: Full access to Odoo models, records, and methods
* **XML-RPC Communication**: Secure connection to Odoo instances via XML-RPC
* **Flexible Configuration**: Support for config files and environment variables
* **Resource Pattern System**: URI-based access to Odoo data structures
* **Error Handling**: Clear error messages for common Odoo API issues
* **Stateless Operations**: Clean request/response cycle for reliable integration

## Tools

* **execute_method**
  * Execute a custom method on an Odoo model
  * Inputs:
    * `model` (string): The model name (e.g., 'res.partner')
    * `method` (string): Method name to execute
    * `args` (optional array): Positional arguments
    * `kwargs` (optional object): Keyword arguments
  * Returns: Dictionary with the method result and success indicator

* **search_employee**
  * Search for employees by name
  * Inputs:
    * `name` (string): The name (or part of the name) to search for
    * `limit` (optional number): The maximum number of results to return (default 20)
  * Returns: Object containing success indicator, list of matching employee names and IDs, and any error message

* **search_holidays**
  * Searches for holidays within a specified date range
  * Inputs:
    * `start_date` (string): Start date in YYYY-MM-DD format
    * `end_date` (string): End date in YYYY-MM-DD format
    * `employee_id` (optional number): Optional employee ID to filter holidays
  * Returns: Object containing success indicator, list of holidays found, and any error message

## Resources

* **odoo://models**
  * Lists all available models in the Odoo system
  * Returns: JSON array of model information

* **odoo://model/{model_name}**
  * Get information about a specific model including fields
  * Example: `odoo://model/res.partner`
  * Returns: JSON object with model metadata and field definitions

* **odoo://record/{model_name}/{record_id}**
  * Get a specific record by ID
  * Example: `odoo://record/res.partner/1`
  * Returns: JSON object with record data

* **odoo://search/{model_name}/{domain}**
  * Search for records that match a domain
  * Example: `odoo://search/res.partner/[["is_company","=",true]]`
  * Returns: JSON array of matching records (limited to 10 by default)

## Configuration

### Odoo Connection Setup

1. Create a configuration file named `odoo_config.json`:
=======

# Odoo MCP Improved

![demo.gif](demo.gif)

<div align="center">

![Odoo MCP Improved Logo](https://img.shields.io/badge/Odoo%20MCP-Improved-brightgreen?style=for-the-badge&logo=odoo)

[![PyPI version](https://img.shields.io/badge/pypi-v1.0.0-blue.svg)](https://pypi.org/project/odoo-mcp-improved/)
[![Python Versions](https://img.shields.io/badge/python-3.8%20%7C%203.9%20%7C%203.10%20%7C%203.11-blue)](https://pypi.org/project/odoo-mcp-improved/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](https://opensource.org/licenses/MIT)

**Enhanced Model Context Protocol (MCP) server for Odoo ERP with advanced tools for sales, purchases, inventory and accounting**

</div>

---

## 📋 Table of Contents

- [Overview](#-overview)
- [Features](#-features)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Usage](#-usage)
- [Tools Reference](#-tools-reference)
- [Resources Reference](#-resources-reference)
- [Prompts](#-prompts)
- [Claude Desktop Integration](#-claude-desktop-integration)
- [License](#-license)

---

## 🔍 Overview

Odoo MCP Improved is a comprehensive implementation of the [Model Context Protocol (MCP)](https://modelcontextprotocol.io/) for Odoo ERP systems. It provides a bridge between large language models like Claude and your Odoo instance, enabling AI assistants to interact directly with your business data and processes.

This extended version enhances the original MCP-Odoo implementation with advanced tools and resources for sales, purchases, inventory management, and accounting, making it a powerful solution for AI-assisted business operations.

---

## ✨ Features

### Core Capabilities
- **Seamless Odoo Integration**: Connect directly to your Odoo instance via XML-RPC
- **Comprehensive Data Access**: Query and manipulate data across all Odoo modules
- **Modular Architecture**: Easily extensible with new tools and resources
- **Robust Error Handling**: Clear error messages and validation for reliable operation

### Business Domain Support
- **Sales Management**: Order tracking, customer insights, and performance analysis
- **Purchase Management**: Supplier management, order processing, and performance metrics
- **Inventory Management**: Stock monitoring, inventory adjustments, and turnover analysis
- **Accounting**: Financial reporting, journal entries, and ratio analysis

### Advanced Functionality
- **Analytical Tools**: Business intelligence capabilities across all domains
- **Specialized Prompts**: Pre-configured prompts for common business scenarios
- **Resource URIs**: Standardized access to Odoo data through URI patterns
- **Performance Optimization**: Caching and efficient data retrieval

---

## 📦 Installation

### Using pip

```bash
pip install odoo-mcp-improved
```

### From Source

```bash
git clone https://github.com/hachecito/odoo-mcp-improved.git
cd odoo-mcp-improved
pip install -e .
```

---

## ⚙️ Configuration

### Environment Variables

```bash
export ODOO_URL=https://your-odoo-instance.com
export ODOO_DB=your_database
export ODOO_USERNAME=your_username
export ODOO_PASSWORD=your_password
```

### Configuration File

Create an `odoo_config.json` file in your working directory:
>>>>>>> hachecito/main

```json
{
  "url": "https://your-odoo-instance.com",
<<<<<<< HEAD
  "db": "your-database-name",
  "username": "your-username",
  "password": "your-password-or-api-key"
}
```

2. Alternatively, use environment variables:
   * `ODOO_URL`: Your Odoo server URL
   * `ODOO_DB`: Database name
   * `ODOO_USERNAME`: Login username
   * `ODOO_PASSWORD`: Password or API key
   * `ODOO_TIMEOUT`: Connection timeout in seconds (default: 30)
   * `ODOO_VERIFY_SSL`: Whether to verify SSL certificates (default: true)
   * `HTTP_PROXY`: Force the ODOO connection to use an HTTP proxy

### Usage with Claude Desktop

Add this to your `claude_desktop_config.json`:
=======
  "db": "your_database",
  "username": "your_username",
  "password": "your_password"
}
```

---

## 🚀 Usage

### Running the Server

```bash
# Using the module
python -m odoo_mcp
```

### Example Interactions

```
# Sales Analysis
Using the Odoo MCP, analyze our sales performance for the last quarter and identify our top-selling products.

# Inventory Check
Check the current stock levels for product XYZ across all warehouses.

# Financial Analysis
Calculate our current liquidity and profitability ratios based on the latest financial data.

# Customer Insights
Provide insights on customer ABC's purchase history and payment patterns.
```

---

## 🤖 Claude Desktop Integration

Add the following to your `claude_desktop_config.json`:
>>>>>>> hachecito/main

```json
{
  "mcpServers": {
    "odoo": {
      "command": "python",
<<<<<<< HEAD
      "args": [
        "-m",
        "odoo_mcp"
      ],
      "env": {
        "ODOO_URL": "https://your-odoo-instance.com",
        "ODOO_DB": "your-database-name",
        "ODOO_USERNAME": "your-username",
        "ODOO_PASSWORD": "your-password-or-api-key"
=======
      "args": ["-m", "odoo_mcp"],
      "env": {
        "ODOO_URL": "https://your-odoo-instance.com",
        "ODOO_DB": "your_database",
        "ODOO_USERNAME": "your_username",
        "ODOO_PASSWORD": "your_password"
>>>>>>> hachecito/main
      }
    }
  }
}
```

<<<<<<< HEAD
### Docker

```json
{
  "mcpServers": {
    "odoo": {
      "command": "docker",
      "args": [
        "run",
        "-i",
        "--rm",
        "-e",
        "ODOO_URL",
        "-e",
        "ODOO_DB",
        "-e",
        "ODOO_USERNAME",
        "-e",
        "ODOO_PASSWORD",
        "mcp/odoo"
      ],
      "env": {
        "ODOO_URL": "https://your-odoo-instance.com",
        "ODOO_DB": "your-database-name",
        "ODOO_USERNAME": "your-username",
        "ODOO_PASSWORD": "your-password-or-api-key"
      }
    }
  }
}
```

## Installation

### Python Package

```bash
pip install odoo-mcp
```

### Running the Server

```bash
# Using the installed package
odoo-mcp

# Using the MCP development tools
mcp dev odoo_mcp/server.py

# With additional dependencies
mcp dev odoo_mcp/server.py --with pandas --with numpy

# Mount local code for development
mcp dev odoo_mcp/server.py --with-editable .
```

## Build

Docker build:

```bash
docker build -t mcp/odoo:latest -f Dockerfile .
```

## Parameter Formatting Guidelines

When using the MCP tools for Odoo, pay attention to these parameter formatting guidelines:

1. **Domain Parameter**:
   * The following domain formats are supported:
     * List format: `[["field", "operator", value], ...]`
     * Object format: `{"conditions": [{"field": "...", "operator": "...", "value": "..."}]}`
     * JSON string of either format
   * Examples:
     * List format: `[["is_company", "=", true]]`
     * Object format: `{"conditions": [{"field": "date_order", "operator": ">=", "value": "2025-03-01"}]}`
     * Multiple conditions: `[["date_order", ">=", "2025-03-01"], ["date_order", "<=", "2025-03-31"]]`

2. **Fields Parameter**:
   * Should be an array of field names: `["name", "email", "phone"]`
   * The server will try to parse string inputs as JSON

## License

This MCP server is licensed under the MIT License.
=======
---

## 🛠️ Tools Reference

### Sales Tools

| Tool | Description |
|------|-------------|
| `search_sales_orders` | Search for sales orders with advanced filtering |
| `create_sales_order` | Create a new sales order |
| `analyze_sales_performance` | Analyze sales performance by period, product, or customer |
| `get_customer_insights` | Get detailed insights about a specific customer |

### Purchase Tools

| Tool | Description |
|------|-------------|
| `search_purchase_orders` | Search for purchase orders with advanced filtering |
| `create_purchase_order` | Create a new purchase order |
| `analyze_supplier_performance` | Analyze supplier performance metrics |

### Inventory Tools

| Tool | Description |
|------|-------------|
| `check_product_availability` | Check stock availability for products |
| `create_inventory_adjustment` | Create inventory adjustment entries |
| `analyze_inventory_turnover` | Calculate and analyze inventory turnover metrics |

### Accounting Tools

| Tool | Description |
|------|-------------|
| `search_journal_entries` | Search for accounting journal entries |
| `create_journal_entry` | Create a new journal entry |
| `analyze_financial_ratios` | Calculate key financial ratios |

---

## 🔗 Resources Reference

### Sales Resources

| URI | Description |
|-----|-------------|
| `odoo://sales/orders` | List sales orders |
| `odoo://sales/order/{order_id}` | Get details of a specific sales order |
| `odoo://sales/products` | List sellable products |
| `odoo://sales/customers` | List customers |

### Purchase Resources

| URI | Description |
|-----|-------------|
| `odoo://purchase/orders` | List purchase orders |
| `odoo://purchase/order/{order_id}` | Get details of a specific purchase order |
| `odoo://purchase/suppliers` | List suppliers |

### Inventory Resources

| URI | Description |
|-----|-------------|
| `odoo://inventory/products` | List products in inventory |
| `odoo://inventory/stock/{location_id}` | Get stock levels at a specific location |
| `odoo://inventory/movements` | List inventory movements |

### Accounting Resources

| URI | Description |
|-----|-------------|
| `odoo://accounting/accounts` | List accounting accounts |
| `odoo://accounting/journal_entries` | List journal entries |
| `odoo://accounting/reports/{report_type}` | Get financial reports |

---

## 💬 Prompts

Odoo MCP Improved includes specialized prompts for different business scenarios:

### Sales Analysis Prompts
- Sales trend analysis
- Customer segmentation
- Product performance evaluation
- Sales team performance

### Inventory Management Prompts
- Stock optimization
- Reordering suggestions
- Warehouse efficiency analysis
- Product movement patterns

### Human Resources Prompts
- Staff planning
- Scheduling optimization
- Performance evaluation
- Resource allocation

### Financial Analysis Prompts
- Ratio interpretation
- Cash flow analysis
- Budget variance analysis
- Financial health assessment

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

This repo is extended from [mcp-odoo](https://github.com/tuanle96/mcp-odoo) - [Lê Anh Tuấn](https://github.com/tuanle96)

---

<div align="center">

**Odoo MCP Improved** - Empowering AI assistants with comprehensive Odoo ERP capabilities

</div>
>>>>>>> hachecito/main
