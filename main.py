"""Test script for calendar date utilities."""

from src.calendar_mcp_server.date_utils import (
    get_current_date,
    get_day_of_week,
    get_week_range,
    calculate_date_offset,
    is_same_week,
    get_week_number,
    days_between,
)


def test_current_date():
    print("=== Current Date ===")
    result = get_current_date()
    print(f"Today: {result['date']}")
    print(f"Day: {result['day_name']} (#{result['day_number']})")
    print(f"Week {result['week_number']}, {result['year']}")
    print(f"Weekend: {result['is_weekend']}")
    print()


def test_day_of_week():
    print("=== Day of Week ===")
    result = get_day_of_week("2026-02-18")
    print(f"2026-02-18 is a {result['day_name']}")
    print()


def test_week_range():
    print("=== Week Range ===")
    result = get_week_range("2026-02-18")
    print(f"Week for 2026-02-18: {result['monday']} to {result['sunday']}")
    print()


def test_date_offset():
    print("=== Date Offset ===")
    print(f"7 days from 2026-02-18: {calculate_date_offset('2026-02-18', 7)}")
    print(f"7 days before 2026-02-18: {calculate_date_offset('2026-02-18', -7)}")
    print()


def test_same_week():
    print("=== Same Week Check ===")
    print(f"2026-02-16 and 2026-02-18 same week? {is_same_week('2026-02-16', '2026-02-18')}")
    print(f"2026-02-16 and 2026-02-23 same week? {is_same_week('2026-02-16', '2026-02-23')}")
    print()


def test_week_number():
    print("=== Week Number ===")
    result = get_week_number("2026-02-18")
    print(f"2026-02-18 is in week {result['week']} of {result['year']}")
    print()


def test_days_between():
    print("=== Days Between ===")
    print(f"Days from 2026-02-16 to 2026-02-22: {days_between('2026-02-16', '2026-02-22')}")
    print(f"Days from 2026-02-22 to 2026-02-16: {days_between('2026-02-22', '2026-02-16')}")
    print()


if __name__ == "__main__":
    print("Testing Calendar Date Utilities\n")
    test_current_date()
    test_day_of_week()
    test_week_range()
    test_date_offset()
    test_same_week()
    test_week_number()
    test_days_between()
    print("All tests completed!")