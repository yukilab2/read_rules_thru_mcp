## Service Specification

This server is an MCP (Model Context Protocol) server designed to provide rule data to AI clients such as Cursor and VSCode.

### Features (Tools)

#### `read_rule_from_uris`
- This tool reads rules from the document URIs provided as parameters and returns them to the MCP client.
- Currently, URIs requiring authentication are not supported (support planned for the future).

### Technical Stack


- Python 3.12+
- pacakge manager: uv
    - FastAPI
    - MCP Python SDK ([modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk))

### applicable rule

./test_rules/myrule.md

