import os
from pymongo import MongoClient

uri = "mongodb+srv://ajaxuser:9JuTJyav69d0okOC@cluster0.rkqjig4.mongodb.net/?appName=Cluster0"

try:
    print("📡 Connecting directly to Atlas cluster...")
    client = MongoClient(uri)
    
    # List all database names visible to this user
    db_names = client.list_database_names()
    print(f"📁 Visible databases in your cluster: {db_names}")
    
    # Check the 'nexusflow' database specifically
    db = client["nexusflow"]
    print(f"🗂️ Collections inside 'nexusflow' database: {db.list_collection_names()}")
    
    # Check if SHIP-9081 exists anywhere
    shipment = db["shipments"].find_one({"_id": "SHIP-9081"})
    if shipment:
        print(f"✅ Found Shipment: SHIP-9081 | Status: {shipment.get('status')}")
    else:
        print("❌ Shipment 'SHIP-9081' does not exist in 'nexusflow.shipments' collection yet.")

except Exception as e:
    print(f"❌ Diagnostic Error: {e}")
