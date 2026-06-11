import os
from pymongo import MongoClient

# Connect directly using your connection string
uri = "mongodb+srv://ajaxuser:9JuTJyav69d0okOC@cluster0.v9qxp.mongodb.net/?retryWrites=true&w=majority"

try:
    client = MongoClient(uri)
    # Target the specific database named in your Cloud Run setup
    db = client["nexusflow"]
    
    print("📋 Checking 'shipments' collection...")
    shipment = db["shipments"].find_one({"_id": "SHIP-9081"})
    if shipment:
        print(f" -> Found Shipment SHIP-9081!")
        print(f" -> Current Status in DB: {shipment.get('status')}")
        print(f" -> Current Destination in DB: {shipment.get('destination')}")
    else:
        print(" -> Shipment SHIP-9081 not found in the 'nexusflow' database.")
        
    print("\n📋 Checking 'incidents' collection...")
    incident_count = db["incidents"].count_documents({})
    print(f" -> Total logs found in incidents: {incident_count}")
    for doc in db["incidents"].find().limit(2):
        print(f"   - Logged Scenario: {doc.get('scenario')}")

except Exception as e:
    print(f"❌ Connection Error: {e}")
