"""Calendar MCP Server - Exposes date utilities via MCP protocol."""

from mcp.server.fastmcp import FastMCP
from calendar_mcp_server import date_utils

mcp = FastMCP("calendar")


@mcp.tool()
async def get_current_date() -> dict:
    """Returns today's date and metadata."""
    return date_utils.get_current_date()


@mcp.tool()
async def get_day_of_week(date: str) -> dict:
    """Get day of week for a given date.

    Args:
        date: Date in YYYY-MM-DD format
    """
    return date_utils.get_day_of_week(date)


@mcp.tool()
async def get_week_range(date: str) -> dict:
    """Returns Monday-Sunday range for a given date.

    Args:
        date: Date in YYYY-MM-DD format
    """
    return date_utils.get_week_range(date)


@mcp.tool()
async def calculate_date_offset(date: str, days: int) -> str:
    """Add or subtract days from a date.

    Args:
        date: Date in YYYY-MM-DD format
        days: Number of days to add (positive) or subtract (negative)
    """
    return date_utils.calculate_date_offset(date, days)


@mcp.tool()
async def is_same_week(date1: str, date2: str) -> bool:
    """Check if two dates are in the same week.

    Args:
        date1: First date in YYYY-MM-DD format
        date2: Second date in YYYY-MM-DD format
    """
    return date_utils.is_same_week(date1, date2)


@mcp.tool()
async def get_week_number(date: str) -> dict:
    """Returns ISO week number and year.

    Args:
        date: Date in YYYY-MM-DD format
    """
    return date_utils.get_week_number(date)


@mcp.tool()
async def days_between(start_date: str, end_date: str) -> int:
    """Calculate days between two dates.

    Args:
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
    """
    return date_utils.days_between(start_date, end_date)


if __name__ == "__main__":
    mcp.run()