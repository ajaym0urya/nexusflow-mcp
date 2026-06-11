import httpx
import json

MCP_URL = "https://nexusflow-mcp-bridge-840151967313.us-central1.run.app/mcp"

print("📡 Connecting to live Cloud Run MCP Server Stream...")

with httpx.stream("POST", MCP_URL, json={
    "method": "tools/call",
    "params": {
        "name": "find_documents",
        "arguments": {
            "collection": "shipments",
            "query": {"_id": "SHIP-9081"}
        }
    }
}, headers={"Accept": "text/event-stream, application/json"}) as r:
    print(f"Status Code received from server: {r.status_code}")
    print("\n📝 Live Server Stream Output Data:")
    for line in r.iter_lines():
        if line:
            print(line)
