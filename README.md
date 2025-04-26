# rule_mcp

## Overview

`rule_mcp` is a project designed to provide rule data to AI clients such as Cursor and VSCode.

## How to Use

```bash
uv install
uv run main.py
```

Now MPC server is runing at http://localhost:8123/mcp

How to set up mpc.json

```json
{
  "mcpServers": {
    "rule-mcp": {
      "url": "http://localhost:8123/mcp"
    }
  }
}
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the MIT - see the LICENSE file for details.

