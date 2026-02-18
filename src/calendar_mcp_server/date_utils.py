"""Core date and calendar utility functions."""

from datetime import datetime, timedelta


def get_current_date() -> dict:
    """Get current date with metadata."""
    today = datetime.now()
    return {
        "date": today.strftime("%Y-%m-%d"),
        "day_name": today.strftime("%A"),
        "day_number": today.isoweekday(),
        "week_number": today.isocalendar()[1],
        "year": today.year,
        "month": today.month,
        "is_weekend": today.isoweekday() in [6, 7],
    }


def get_day_of_week(date: str) -> dict:
    """Get day of week for a given date."""
    dt = datetime.strptime(date, "%Y-%m-%d")
    return {
        "date": date,
        "day_name": dt.strftime("%A"),
        "day_number": dt.isoweekday(),
        "is_weekend": dt.isoweekday() in [6, 7],
    }


def get_week_range(date: str) -> dict:
    """Get Monday-Sunday range for a given date."""
    dt = datetime.strptime(date, "%Y-%m-%d")
    monday = dt - timedelta(days=dt.isoweekday() - 1)
    sunday = monday + timedelta(days=6)
    return {
        "monday": monday.strftime("%Y-%m-%d"),
        "sunday": sunday.strftime("%Y-%m-%d"),
    }


def calculate_date_offset(date: str, days: int) -> str:
    """Add/subtract days from a date."""
    dt = datetime.strptime(date, "%Y-%m-%d")
    new_dt = dt + timedelta(days=days)
    return new_dt.strftime("%Y-%m-%d")


def is_same_week(date1: str, date2: str) -> bool:
    """Check if two dates are in the same week."""
    dt1 = datetime.strptime(date1, "%Y-%m-%d")
    dt2 = datetime.strptime(date2, "%Y-%m-%d")
    return dt1.isocalendar()[:2] == dt2.isocalendar()[:2]


def get_week_number(date: str) -> dict:
    """Get ISO week number and year."""
    dt = datetime.strptime(date, "%Y-%m-%d")
    iso_cal = dt.isocalendar()
    return {"week": iso_cal[1], "year": iso_cal[0]}


def days_between(start_date: str, end_date: str) -> int:
    """Calculate days between two dates."""
    dt1 = datetime.strptime(start_date, "%Y-%m-%d")
    dt2 = datetime.strptime(end_date, "%Y-%m-%d")
    return (dt2 - dt1).days