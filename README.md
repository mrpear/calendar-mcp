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
      "command": "/Users/<USERNAME>/.local/bin/uv",
      "args": [
        "--directory",
        "/Users/pgruszka/PycharmProjects/calendar-mcp",
        "run",
        "--with",
        "mcp[cli]",
        "mcp",
        "run",
        "/Users/pgruszka/PycharmProjects/calendar-mcp/src/calendar_mcp_server/server.py"
      ]
    }
  }
}
```

**Notes:**
- Replace `/Users/pgruszka/PycharmProjects/calendar-mcp` with your actual path
- Find `uv` path with: `which uv`
- Restart Claude Code after configuration

## Usage Example

```
User: "What workouts do I have this week?"

Claude calls: mcp__calendar__get_week_range(date="2026-02-18")
Server returns: {"monday": "2026-02-16", "sunday": "2026-02-22"}

Claude calls: mcp__intervals-icu__get_events(start_date="2026-02-16", end_date="2026-02-22")
Claude responds: "This week (Feb 16-22) you have workouts on..."
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