# NexusFlow

> AI-Powered Autonomous Logistics Recovery Engine for Cold-Chain Supply Networks

NexusFlow is an intelligent logistics resilience platform designed to detect, analyze, and autonomously mitigate cold-chain transportation failures in real time.

Built using **Google Gemini**, **Vertex AI**, **MongoDB Atlas**, and a custom **MCP (Model Context Protocol) Bridge**, NexusFlow continuously monitors shipment telemetry and executes recovery actions before temperature-sensitive cargo becomes unusable.

---

# 🚀 Features

- Real-time shipment monitoring
- Autonomous incident detection
- AI-powered recovery planning
- Geospatial warehouse selection
- MongoDB Atlas operational persistence
- Immutable incident audit trail
- Vertex AI Gemini agent orchestration
- Cloud Run MCP integration

---

# 🏗️ Architecture Overview

```text
Shipment Telemetry
        │
        ▼
 Gemini Agent (Vertex AI)
        │
        ▼
 MCP Bridge (Cloud Run)
        │
 ┌──────┴────────┐
 ▼               ▼
MongoDB Atlas   Recovery Logic
        │
        ▼
 Autonomous Mitigation
```

---

# 📊 Database Schema Blueprint

NexusFlow utilizes three primary MongoDB Atlas collections.

## 1️⃣ shipments Collection

Stores active shipment metadata, temperature thresholds, geolocation data, and routing information.

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
```

---

## 2️⃣ hubs Collection

Maintains certified warehouse facilities available for emergency rerouting.

```json
{
  "_id": "HUB-4402",
  "name": "SafeCold Storage Newark",
  "certificates": [
    "Biologics",
    "DeepFreeze"
  ],
  "location": {
    "type": "Point",
    "coordinates": [-74.1724, 40.7357]
  },
  "capacity": "AVAILABLE"
}
```

---

## 3️⃣ incidents Collection

Immutable operational ledger containing every automated intervention performed by NexusFlow.

```json
{
  "_id": "INC-1001",
  "shipment_id": "SHIP-9081",
  "event_type": "TEMPERATURE_BREACH",
  "action": "REROUTED",
  "timestamp": "2026-06-10T14:32:21Z"
}
```

---

# 📂 Repository Structure

```text
nexusflow-mcp/
│
├── agent.py
│   └── Gemini Agent execution entrypoint
│
├── index.js
│   └── MCP HTTP Server implementation
│
├── package.json
│   └── Node.js configuration and dependencies
│
├── package-lock.json
│   └── Dependency lockfile
│
└── LICENSE
    └── MIT License
```

---

# ⚡ Runtime Demonstration

Example execution trace when NexusFlow detects a temperature breach.

```bash
$ python3 agent.py

🚀 Connecting to Cloud Run MCP Bridge...

🧠 Initializing Gemini Recovery Engine...

🧠 Incident Detected:
Shipment SHIP-9081 exceeded safe operating threshold.

Current Temperature:
-11.2°C

Allowed Maximum:
-15°C

Initiating autonomous recovery workflow...

💾 Executing MongoDB operations...

→ Fetching shipment metadata...
→ Identifying certified backup facilities...
→ Calculating nearest compliant warehouse...
→ Updating shipment routing...

✅ Shipment successfully rerouted.

→ Logging intervention in incidents collection...

✅ Recovery process completed.
```

---

# 🔄 Resulting Database Mutations

## Shipment Update

The shipment record is automatically modified:

```json
{
  "_id": "SHIP-9081",
  "status": "REROUTED",
  "destination": "SafeCold Storage Newark"
}
```

## Incident Log Entry

A new immutable audit record is created:

```json
{
  "_id": "INC-1001",
  "shipment_id": "SHIP-9081",
  "action": "REROUTED",
  "reason": "TEMPERATURE_BREACH"
}
```

---

# 💻 Local Development Setup

## Prerequisites

- Python 3.12+
- Node.js v18+
- MongoDB Atlas Cluster
- Google Cloud Project
- Vertex AI Enabled
- Google Cloud CLI (`gcloud`)

---

## Clone Repository

```bash
git clone https://github.com/ajaym0urya/nexusflow-mcp.git

cd nexusflow-mcp
```

---

## Install Python Dependencies

```bash
pip install google-genai httpx
```

---

## Install Node Dependencies

```bash
npm install
```

---

## Configure Google Cloud

Authenticate locally:

```bash
gcloud auth application-default login
```

Set your project:

```bash
gcloud config set project YOUR_PROJECT_ID
```

---

## Run NexusFlow Agent

```bash
python3 agent.py
```

---

# 🛠️ Technology Stack

| Layer | Technology |
|---------|------------|
| AI Agent | Gemini |
| Agent Runtime | Vertex AI |
| Database | MongoDB Atlas |
| Server Layer | Node.js |
| MCP Transport | HTTP MCP Bridge |
| Hosting | Cloud Run |
| Language | Python + JavaScript |

---

# 🎯 Use Cases

- Vaccine transportation monitoring
- Pharmaceutical logistics
- Cold-chain food distribution
- Medical supply transportation
- High-value perishable goods tracking

---

# 🔐 Security & Compliance

NexusFlow maintains a complete operational audit trail through immutable incident records, ensuring:

- Traceability
- Regulatory compliance
- Recovery transparency
- Operational accountability

---

# 📜 License

Released under the MIT License.

See the `LICENSE` file for details.

---

## Built for resilient global supply chains 🌎
