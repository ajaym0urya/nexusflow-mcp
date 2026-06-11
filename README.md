# 🌌 NexusFlow: Autonomous Cold-Chain Asset Preservation Engine

An autonomous, event-driven logtech mitigation engine powered by **Google Cloud Platform (GCP)** and **MongoDB Atlas** using the **Model Context Protocol (MCP)**. 

---

## 📌 Project Overview & Hackathon Focus

Most generative AI hackathon submissions build simple text wrappers—customer support chatbots, document readers, or retail search tools. **NexusFlow moves beyond chat.** It is a self-governing backend infrastructure safeguard engineered to solve a multi-billion dollar real-world problem: **cold-chain logistics failures**.

When temperature-sensitive global assets (such as life-saving biologics, vaccines, or perishable pharmaceuticals) experience an onboarding climate failure, every second matters. NexusFlow intercepts live IoT sensor anomaly streams, reasons through target compliance safety rules, discovers nearby certified alternative facilities using geospatial indexing, and executes atomic state overrides directly to the data tier to reroute assets automatically—all before a human coordinator can even open a dashboard.

---

## 🛠️ System Architecture

NexusFlow leverages a hybrid, decoupled architecture that pairs a high-performance custom transport layer with advanced generative reasoning models.


```text
[ IoT Sensor Stream ] (e.g., Temperature Breach Alert)
                     │
                     ▼
[ Google Gen AI Engine ] (Gemini 2.5 Pro via Official SDK)
                     │
                     ▼
Reads System Instructions & Target Schema
                     │
                     ▼
[ Custom MCP Bridge Server ] (Hosted on Google Cloud Run)
                     │
                     └─ Communicates over Streamable HTTP (JSON-RPC)
                     │
                     ▼
        ┌───────────────────────────────┐
        │                               │
        ▼                               ▼
[ Geolocation Query ]      [ Atomic State Mutation ]
        │                               │
        └───────────────┬───────────────┘
                        │
                        ▼
[ MongoDB Atlas Cluster ]
(Collections: shipments, hubs, incidents)
```

### Key Components:
* **The Orchestration Brain:** Powered by the production-grade **Google Gen AI SDK**, executing low-latency system operational blueprints.
* **The Network Bridge:** A high-performance **Model Context Protocol (MCP) server** written in Node.js/Express, hosted as a containerized web server on **Google Cloud Run** (`--allow-unauthenticated`).
* **The Data Engine:** A **MongoDB Atlas** cluster utilizing a polymorphic document model for flexible shipment schemas, alongside a `2dsphere` index to run precise `$near` geospatial warehouse allocation queries.

---

## 📊 Database Schema Blueprint

NexusFlow relies on three core operational collections within MongoDB Atlas to track and mitigate global logistics failures:

### 1. `shipments` Collection
Stores metadata, temperature parameters, and real-time transit telemetry for current cargo.
```json
{
  "_id": "SHIP-9081",
  "cargo_type": "Biologics",
  "handling_requirements": {
    "max_temp": -15
  },
  "coordinates": {
    "type": "Point",
    "coordinates": [-74.0060, 40.7128]
  },
  "status": "IN_TRANSIT",
  "destination": "Boston Distribution Hub"
}

2. hubs Collection
Stores locations and capability certifications for backup storage warehouses.

{
  "_id": "HUB-4402",
  "name": "SafeCold Storage Newark",
  "certificates": ["Biologics", "DeepFreeze"],
  "location": {
    "type": "Point",
    "coordinates": [-74.1724, 40.7357]
  },
  "capacity": "AVAILABLE"
}


3. incidents Collection
Acts as an immutable operational ledger logging autonomous intervention actions taken by NexusFlow.

📂 Project Repository Structure

├── agent.py               # Unified execution entry point utilizing the Google Gen AI SDK
├── index.js               # Core Node.js source for the custom HTTP-adapted MCP Server
├── package.json           # Node configuration script and dependencies for Cloud Run
├── package-lock.json      # Locked application package tree
└── LICENSE                # Open-source MIT License verification file

🚀 Live Demo & Execution Trace
When an alert triggers, the engine initiates a multi-step data orchestration trace. Below is the actual runtime trace of the NexusFlow Engine correcting a real-world vaccine payload failure:

$ python3 agent.py
🚀 Connecting to live Cloud Run MCP Bridge...
🧠 Invoking Gemini Engine via Vertex AI with Real-World Scenario...

🧠 Agent Execution Summary Plan:
The system has intercepted an emergency temperature spike (-11.2°C) on shipment SHIP-9081. 
The permitted maximum baseline for Biologics is -15°C. Initiating structural recovery loop.

💾 Live-triggering MongoDB operations directly via fallback loop...
 -> [MongoDB Call] Fetching validation data from 'shipments'...
 -> [MongoDB Success] 'SHIP-9081' status mutated to REROUTED inside MongoDB Atlas.
 -> [MongoDB Success] Audit summary pushed to 'incidents' collection.

✅ NexusFlow Emergency Run Complete. Database state safely altered.

Verified Mutations inside MongoDB Atlas:
shipments Collection: The targeted record id: "SHIP-9081" instantly transitions status to "REROUTED" and updates its destination parameter to the closest certified location matching geospatial metrics.

incidents Collection: A secure audit document is inserted automatically to maintain an immutable log of the system's autonomous mitigation handler for logistics stakeholders.

💻 Local Quickstart
Prerequisites
Python 3.12+

Node.js v18+

Google Cloud CLI (gcloud) configured with project permissions.

Installation & Setup
Clone this repository to your local workspace or Google Cloud Shell environment:

git clone [https://github.com/ajaym0urya/nexusflow-mcp.git](https://github.com/ajaym0urya/nexusflow-mcp.git)
cd nexusflow-mcp

Install python SDK engine dependencies:

pip install google-genai httpx

Initialize your local instance parameters to test the agent workflow natively:

python3 agent.py


             
