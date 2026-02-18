# Calendar MCP Server

Model Context Protocol server providing calendar and date utilities to help AI models with temporal reasoning.

## Features

- **get_current_date** - Returns today's date with metadata (day name, week number, etc.)
- **get_day_of_week** - Get day name for any date
- **get_week_range** - Get Monday-Sunday range for a date's week
- **calculate_date_offset** - Add/subtract days from a date
- **is_same_week** - Check if two dates are in the same week
- **get_week_number** - Get ISO week number for a date
- **days_between** - Calculate days between two dates

All dates use ISO format: `YYYY-MM-DD`

## Setup

### 1. Install uv

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

### 2. Create virtual environment and install dependencies

```bash
cd /path/to/calendar-mcp
uv venv --python 3.14
source .venv/bin/activate
uv sync
```

### 3. Test the utilities

```bash
python main.py
```

## Claude Code Configuration

Add this to your `~/.claude.json` file:

```json
{
  "mcpServers": {
    "calendar": {
      "type": "stdio",
      "command": "/path/to/uv",
      "args": [
        "--directory",
        "/path/to/calendar-mcp",
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/path/to/calendar-mcp/src/calendar_mcp_server/server.py"
      ]
    }
  }
}
```

**Notes:**
- Replace `/path/to/calendar-mcp` with your actual calendar-mcp directory path
- Replace `/path/to/uv` with your uv binary path (find it with: `which uv`)
- Restart Claude Code after configuration

## Usage Example

```
User: "What is today's date and what week is it?"

Claude calls: mcp__calendar__get_current_date()
Server returns: {"date": "2026-02-18", "day_name": "Wednesday", "week_number": 8, ...}

Claude responds: "Today is Wednesday, February 18th, 2026 (week 8)."
```

## Available Tools

All tools are prefixed with `mcp__calendar__`:

- `mcp__calendar__get_current_date()` → Returns current date info
- `mcp__calendar__get_day_of_week(date)` → Day name (e.g., "Wednesday")
- `mcp__calendar__get_week_range(date)` → Week boundaries
- `mcp__calendar__calculate_date_offset(date, days)` → New date
- `mcp__calendar__is_same_week(date1, date2)` → Boolean
- `mcp__calendar__get_week_number(date)` → Week number and year
- `mcp__calendar__days_between(start_date, end_date)` → Integer

## Development

The core logic is in `src/calendar_mcp_server/date_utils.py` as simple Python functions.
The MCP server wrapper is in `src/calendar_mcp_server/server.py`.

## License

MIT