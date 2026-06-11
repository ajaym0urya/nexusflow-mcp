import express from 'express';
import { MongoClient } from 'mongodb';
import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js';
import { StreamableHTTPServerTransport } from '@modelcontextprotocol/sdk/server/streamableHttp.js';

const app = express();
app.use(express.json());

// Initialize MongoDB Connection using environment variable
const client = new MongoClient(process.env.MONGODB_URI);
let db;

async function initMongo() {
  await client.connect();
  db = client.db('nexusflow');
  console.log('Connected to MongoDB Database: nexusflow');
}
initMongo().catch(console.error);

// Create the MCP Server
const server = new McpServer({
  name: "nexusflow-mcp-engine",
  version: "1.0.0"
});

// Tool 1: Find Active Shipments or Hubs
server.tool("find_documents", async ({ collection, filter }) => {
  const targetCollection = db.collection(collection);
  const data = await targetCollection.find(filter || {}).toArray();
  return { content: [{ type: "text", text: JSON.stringify(data) }] };
});

// Tool 2: Update Data State (Rerouting)
server.tool("update_document", async ({ collection, id, updateData }) => {
  const targetCollection = db.collection(collection);
  const result = await targetCollection.updateOne({ _id: id }, { $set: updateData });
  return { content: [{ type: "text", text: `Matched: ${result.matchedCount}, Modified: ${result.modifiedCount}` }] };
});

// Tool 3: Insert Incident Audit Logs
server.tool("insert_document", async ({ collection, document }) => {
  const targetCollection = db.collection(collection);
  const result = await targetCollection.insertOne(document);
  return { content: [{ type: "text", text: `Inserted document with ID: ${result.insertedId}` }] };
});

// Tool 4: Geospatial Backup Search ( query)
server.tool("find_nearby_hubs", async ({ lng, lat, required_cert }) => {
  const targetCollection = db.collection('hubs');
  const query = {
    location: {
      $near: {
        $geometry: { type: "Point", coordinates: [lng, lat] },
        $maxDistance: 32186 // 20 Miles in meters
      }
    },
    certified_for: required_cert
  };
  const data = await targetCollection.find(query).toArray();
  return { content: [{ type: "text", text: JSON.stringify(data) }] };
});

// Bind MCP to Express HTTP Routes
const transport = new StreamableHTTPServerTransport({ sessionIdGenerator: undefined });
await server.connect(transport);

app.post('/mcp', async (req, res) => { await transport.handleRequest(req, res); });
app.get('/mcp', async (req, res) => { await transport.handleRequest(req, res); });

const PORT = process.env.PORT || 8080;
app.listen(PORT, () => {
  console.log(`NexusFlow MCP Server listening on port ${PORT}`);
});
