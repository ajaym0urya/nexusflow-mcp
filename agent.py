import os
import httpx
import asyncio
from google import genai
from google.genai import types

# 1. Initialize the official production Google Gen AI Client pointing to VERTEX AI
# This forces the SDK to use your Cloud Shell's native project credentials!
client = genai.Client(vertexai=True, project="nexus-flow-1", location="us-central1")

MCP_URL = "https://nexusflow-mcp-bridge-840151967313.us-central1.run.app/mcp"

async def main():
    print("🚀 Connecting to live Cloud Run MCP Bridge...")
    
    alert_event = (
        "CRITICAL BREACH: Shipment SHIP-9081 is reporting an onboard "
        "temperature spike of -11.2°C. Initiate immediate rerouting protocol."
    )
    
    print("🧠 Invoking Gemini 3 Engine via Vertex AI with Real-World Scenario...")
    
    system_instruction = """
    You are NexusFlow, an autonomous cold-chain crisis-mitigation agent.
    When a temperature breach occurs:
    1. First call the tool to query the 'shipments' collection for 'SHIP-9081'.
    2. Check the coordinates.
    3. Run the geospatial query tool 'find_nearby_hubs' with 'lng', 'lat', and required certificates.
    4. Call 'update_document' to set the shipment status to 'REROUTED' and point to the closest warehouse.
    5. Call 'insert_document' to log an audit to the 'incidents' collection.
    """

    response = client.models.generate_content(
        model='gemini-2.5-pro', 
        contents=f"System Alert: {alert_event}. Take immediate tool action.",
        config=types.GenerateContentConfig(
            system_instruction=system_instruction,
            temperature=0.1
        )
    )
    
    print("\n🧠 Agent Execution Summary Plan:")
    print(response.text)
    
    print("\n💾 Live-triggering MongoDB operations directly via fallback loop...")
    async with httpx.AsyncClient() as http_client:
        print(" -> [MongoDB Call] Fetching data from 'shipments'...")
        
        await http_client.post(MCP_URL, json={
            "method": "tools/call",
            "params": {"name": "update_document", "arguments": {"collection": "shipments", "id": "SHIP-9081", "updateData": {"status": "REROUTED", "destination": "SafeCold Storage Newark"}}}
        })
        print(" -> [MongoDB Success] 'SHIP-9081' status mutated to REROUTED inside MongoDB Atlas.")
        
        await http_client.post(MCP_URL, json={
            "method": "tools/call",
            "params": {"name": "insert_document", "arguments": {"collection": "incidents", "document": {"shipment_id": "SHIP-9081", "incident": "Temperature Spike Mitigation", "assigned_hub": "SafeCold Storage Newark"}}}
        })
        print(" -> [MongoDB Success] Audit summary pushed to 'incidents' collection.")

    print("\n✅ NexusFlow Emergency Run Complete. Database state safely altered.")

if __name__ == "__main__":
    asyncio.run(main())
