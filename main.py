from fastapi import FastAPI
from fastapi_mcp import FastApiMCP
import requests
import uvicorn

app = FastAPI()

@app.get("/read_rule_from_uri")
async def read_rule_from_uri(uri: str):
    """
    Read rules from a list of uris. and return the rules as a list of strings.
    
    TODO: Support URL. At this point, just relative path to the local files are expected (without file://)
    """
    rules = []
    print("##uri", uri)
    if 0:
        response = requests.get(uri)
        if response.status_code == 200:
            rules.append(response.text)
        else:
            return {"message": "Failed to read rule from uri"}
    else:
        import os
        # FIXME: error handling (security, not-exists.., unneccesary `file://`` prefix...)
        with open(uri, "r") as f:
            rules.append(f.read())
    return {"rules": rules}

mcp = FastApiMCP(app)
mcp.mount()

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8123)
