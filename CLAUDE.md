# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Calendar MCP Server provides date and calendar utilities via the Model Context Protocol. It solves the problem that LLMs struggle with temporal reasoning and date calculations (accuracy ~34% for SOTA models).

**Purpose**: External tools via MCP that handle all date/calendar operations using Python's `datetime` library.

## Architecture

**Two-layer design:**

1. **Core utilities** (`date_utils.py`) - Pure Python functions, no external dependencies
   - All functions are stateless and deterministic
   - Date format: ISO 8601 (`YYYY-MM-DD`)
   - Uses `datetime.strptime()` for parsing, `strftime()` for formatting

2. **MCP wrapper** (`server.py`) - FastMCP async tools that expose utilities
   - Each `@mcp.tool()` decorated function maps to one utility function
   - Tools are automatically prefixed as `mcp__calendar__<function_name>`
   - No error handling in wrapper - exceptions propagate to MCP client

**Key design principle**: Keep date_utils.py simple and testable. All complexity lives in pure Python functions, not in the MCP layer.

## Development Commands

### Setup
```bash
# Create virtual environment (requires Python 3.14+)
uv venv --python 3.14
source .venv/bin/activate

# Install dependencies
uv sync
```

### Testing
```bash
# Run manual tests (outputs to console)
python main.py
```

**Note**: No automated test suite yet. `main.py` provides smoke tests for all utilities.

### MCP Server

The server runs via `uv` when invoked by Claude Code. See README.md for `~/.claude.json` configuration.

**Local testing**: Not currently set up. To test MCP integration, configure in Claude Code and use the tools interactively.

## Date Format Convention

**All dates must be ISO 8601 format: `YYYY-MM-DD`**

- Week starts on Monday (ISO week definition)
- `day_number`: 1=Monday, 7=Sunday
- Week numbers follow ISO 8601 (week 1 contains the first Thursday)

## Adding New Date Utilities

1. Add pure function to `date_utils.py`
   - Input: strings for dates, integers for offsets
   - Output: dict, string, int, or bool
   - Raise `ValueError` for invalid date formats (let `datetime.strptime()` handle this)

2. Add async wrapper to `server.py`
   - Use `@mcp.tool()` decorator
   - Add docstring with Args section (MCP uses this for tool descriptions)
   - Call corresponding `date_utils` function

3. Test manually with `main.py`
   - Add test function following existing pattern
   - Call from `if __name__ == "__main__"` block