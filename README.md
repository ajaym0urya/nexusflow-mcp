# 🌌 NexusFlow: Autonomous Cold-Chain Asset Preservation Engine

> An autonomous, event-driven logistics mitigation engine powered by Google Cloud Platform (GCP), Gemini, and MongoDB Atlas using the Model Context Protocol (MCP).

---

## 📌 Project Overview

Most AI hackathon projects stop at chat interfaces—customer support bots, document assistants, or search applications.

**NexusFlow moves beyond chat.**

NexusFlow is a self-governing backend infrastructure system designed to solve one of the most expensive problems in global supply chains: **cold-chain logistics failures**.

When temperature-sensitive assets such as vaccines, biologics, or pharmaceutical shipments experience environmental anomalies, every minute increases the risk of spoilage and financial loss.

NexusFlow autonomously:

* Detects live temperature breaches from IoT telemetry
* Evaluates compliance and handling requirements
* Identifies nearby certified backup facilities
* Performs geospatial warehouse discovery
* Executes atomic rerouting actions
* Creates immutable audit records

All before a human operator needs to intervene.

---

## 🎯 Problem Statement

Global cold-chain failures result in billions of dollars of losses annually due to:

* Vaccine spoilage
* Pharmaceutical degradation
* Regulatory violations
* Manual operational delays

Current monitoring systems alert humans.

**NexusFlow takes action.**

---

## 🏗️ System Architecture

```text
┌─────────────────────────────┐
│     IoT Sensor Stream       │
│ (Temperature Breach Alert)  │
└─────────────┬───────────────┘
              │
              ▼
┌─────────────────────────────┐
│ Google Gen AI Engine        │
│ Gemini 2.5 Pro              │
└─────────────┬───────────────┘
              │
              ▼
 Reads Operational Instructions
              │
              ▼
┌─────────────────────────────┐
│ Custom MCP Bridge Server    │
│ Google Cloud Run            │
└─────────────┬───────────────┘
              │
     Streamable HTTP / JSON-RPC
              │
              ▼
      ┌───────────────┬───────────────┐
      │               │               │
      ▼               ▼               ▼
Geospatial      State Mutation   Audit Logging
Discovery
      │               │
      └───────┬───────┘
              │
              ▼
┌─────────────────────────────┐
│ MongoDB Atlas Cluster       │
│ shipments                   │
│ hubs                        │
│ incidents                   │
└─────────────────────────────┘
```

---

## ⚙️ Core Components

### 🧠 Orchestration Brain

Powered by the Google Gen AI SDK running Gemini models to execute operational recovery workflows.

### 🌉 MCP Network Bridge

A custom Model Context Protocol (MCP) server built with Node.js and Express, deployed to Google Cloud Run.

Responsibilities:

* Tool execution
* Database operations
* Remote procedure orchestration
* HTTP transport layer

### 🗄️ Data Engine

MongoDB Atlas serves as the operational datastore.

Key capabilities:

* Flexible document schema
* Geospatial indexing (2dsphere)
* Atomic document mutations
* Immutable incident tracking

---

## 📊 Database Schema Blueprint

### 1️⃣ shipments Collection

Stores shipment telemetry and operational metadata.

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

### 2️⃣ hubs Collection

Stores certified warehouse facilities available for emergency rerouting.

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

### 3️⃣ incidents Collection

Maintains an immutable operational audit ledger.

```json
{
  "_id": "INC-1001",
  "shipment_id": "SHIP-9081",
  "action": "REROUTED",
  "reason": "TEMPERATURE_BREACH",
  "timestamp": "2026-06-12T10:30:00Z"
}
```

---

## 📂 Repository Structure

```text
nexusflow-mcp/
│
├── agent.py
│   └── Gemini orchestration engine
│
├── index.js
│   └── MCP server implementation
│
├── package.json
│   └── Node.js configuration
│
├── package-lock.json
│   └── Dependency lock file
│
└── LICENSE
    └── MIT License
```

---

## 🚀 Live Execution Trace

```bash
$ python3 agent.py

🚀 Connecting to Cloud Run MCP Bridge...

🧠 Invoking Gemini Recovery Engine...

🧠 Incident Detected:
Shipment SHIP-9081 exceeded safe operating threshold.

Current Temperature:
-11.2°C

Maximum Allowed:
-15°C

Initiating recovery workflow...

💾 Executing MongoDB operations...

→ Fetching shipment metadata
→ Discovering certified backup hubs
→ Computing nearest compliant facility
→ Updating shipment destination

✅ Shipment rerouted successfully

→ Logging mitigation action

✅ Recovery process completed
```

---

## 🔄 Database Mutations

### Shipment Collection

Before:

```json
{
  "status": "IN_TRANSIT",
  "destination": "Boston Distribution Hub"
}
```

After:

```json
{
  "status": "REROUTED",
  "destination": "SafeCold Storage Newark"
}
```

### Incident Collection

```json
{
  "shipment_id": "SHIP-9081",
  "action": "REROUTED",
  "reason": "TEMPERATURE_BREACH"
}
```

---

## 💻 Local Quickstart

### Prerequisites

* Python 3.12+
* Node.js v18+
* MongoDB Atlas
* Google Cloud Project
* Vertex AI Enabled
* Google Cloud CLI (`gcloud`)

### Clone Repository

```bash
git clone https://github.com/ajaym0urya/nexusflow-mcp.git

cd nexusflow-mcp
```

### Install Python Dependencies

```bash
pip install google-genai httpx
```

### Install Node Dependencies

```bash
npm install
```

### Configure Google Cloud

```bash
gcloud auth application-default login
```

```bash
gcloud config set project YOUR_PROJECT_ID
```

### Run NexusFlow

```bash
python3 agent.py
```

---

## 🛠️ Technology Stack

| Layer          | Technology          |
| -------------- | ------------------- |
| AI Reasoning   | Gemini              |
| AI Runtime     | Vertex AI           |
| Protocol Layer | MCP                 |
| Backend        | Node.js             |
| Database       | MongoDB Atlas       |
| Cloud Platform | Google Cloud Run    |
| Language       | Python & JavaScript |

---

## 🌍 Real-World Applications

* Vaccine distribution
* Pharmaceutical logistics
* Biologics transportation
* Medical cold-chain monitoring
* High-value perishable supply chains

---

## 🔐 Compliance & Auditability

Every automated intervention is permanently recorded within the `incidents` collection, ensuring:

* Operational transparency
* Regulatory traceability
* Compliance reporting
* Stakeholder accountability

---

## 📜 License

Released under the MIT License.

See the `LICENSE` file for details.

---

### Built for resilient, autonomous supply chains 🌎
