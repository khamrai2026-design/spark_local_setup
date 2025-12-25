from tabulate import tabulate
from rich.console import Console
from rich.table import Table
import pandas as pd

# ============================================================================
# Helper Function 1: Simple print with section header
# ============================================================================
def print_section(title, content=None, width=50):
    """
    Print a formatted section with title.
    
    Args:
        title (str): Section title
        content (str/list): Optional content to print
        width (int): Width of the separator line
    
    Example:
        print_section("Results")
        print_section("Data", ["Item 1", "Item 2", "Item 3"])
    """
    print("\n" + "=" * width)
    print(f" {title}")
    print("=" * width)
    if content:
        if isinstance(content, list):
            for item in content:
                print("sss",item)
        else:
            print(content)

# ============================================================================
# Helper Function 2: Print dictionary as aligned key-value pairs
# ============================================================================
def print_dict(data, title=None, key_width=20):
    """
    Print dictionary with nicely aligned key-value pairs.
    
    Args:
        data (dict): Dictionary to print
        title (str): Optional section title
        key_width (int): Width for key column
    
    Example:
        print_dict({"Name": "Alice", "Age": 30, "Score": 95.5}, title="Info")
    """
    if title:
        print_section(title)
    else:
        print()
    for key, value in data.items():
        print(f"{key:.<{key_width}} {value}")

# ============================================================================
# Helper Function 3: Print list of dictionaries as table
# ============================================================================
def print_table(data, title=None, table_format="grid"):
    """
    Print list of dictionaries as a formatted table.
    
    Args:
        data (list): List of dictionaries
        title (str): Optional section title
        table_format (str): "grid", "simple", "plain", "fancy_grid"
    
    Example:
        data = [
            {"Name": "Alice", "Age": 30, "Score": 95.5},
            {"Name": "Bob", "Age": 25, "Score": 88.7}
        ]
        print_table(data, title="Students")
    """
    if title:
        print_section(title)
    else:
        print()
    if data:
        headers = data[0].keys()
        rows = [list(d.values()) for d in data]
        print(tabulate(rows, headers=headers, tablefmt=table_format))

# ============================================================================
# Helper Function 4: Print results with multiple sections
# ============================================================================
def print_results(**sections):
    """
    Print multiple sections at once.
    
    Args:
        **sections: Keyword arguments where key is section title, 
                   value is content
    
    Example:
        print_results(
            Summary="Completed successfully",
            Details=["Item 1", "Item 2"],
            Stats={"Total": 100, "Success": 95}
        )
    """
    for title, content in sections.items():
        if isinstance(content, dict):
            print_dict(content, title=title)
        elif isinstance(content, list) and content and isinstance(content[0], dict):
            print_table(content, title=title)
        else:
            print_section(title, content)

# ============================================================================
# Helper Function 5: Print with rich styling
# ============================================================================
def print_rich_table(data, title=None, columns=None):
    """
    Print table using rich library for styled output.
    
    Args:
        data (list): List of dictionaries
        title (str): Optional table title
        columns (dict): Optional style mapping {column_name: style}
    
    Example:
        data = [
            {"Name": "Alice", "Age": 30, "Score": 95.5},
            {"Name": "Bob", "Age": 25, "Score": 88.7}
        ]
        styles = {"Name": "cyan", "Score": "green"}
        print_rich_table(data, title="Students", columns=styles)
    """
    console = Console()
    table = Table(title=title)
    
    if data:
        headers = data[0].keys()
        
        for header in headers:
            style = columns.get(header, "white") if columns else "white"
            table.add_column(header, style=style)
        
        for row_data in data:
            table.add_row(*[str(v) for v in row_data.values()])
    
    console.print(table)