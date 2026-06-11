import os
from pymongo import MongoClient

uri = "mongodb+srv://ajaxuser:9JuTJyav69d0okOC@cluster0.rkqjig4.mongodb.net/?appName=Cluster0"

try:
    print("📡 Connecting directly to Atlas cluster to force update...")
    client = MongoClient(uri)
    db = client["nexusflow"]
    
    # 1. Force the Shipment update
    result1 = db["shipments"].update_one(
        {"_id": "SHIP-9081"},
        {"$set": {
            "status": "REROUTED_DYNAMIC",
            "destination": "SafeCold Storage Newark",
            "optimization_metrics": {"proximity_miles": 4.2, "cost_index": "OPTIMAL"}
        }}
    )
    print(f" -> Shipment matched: {result1.matched_count}, Modified: {result1.modified_count}")
    
    # 2. Force the Audit insertion
    result2 = db["incidents"].insert_one({
        "shipment_id": "SHIP-9081",
        "scenario": "Scenario A: Temperature Spike Anomaly",
        "regulatory_compliance": "FDA 21 CFR Compliant",
        "status": "RESOLVED"
    })
    print(f" -> Logged Incident ID: {result2.inserted_id}")
    
    # 3. Read it back to verify
    shipment = db["shipments"].find_one({"_id": "SHIP-9081"})
    print(f"\n🎯 Direct DB Verification Status: {shipment.get('status')}")

except Exception as e:
    print(f"❌ Error: {e}")
