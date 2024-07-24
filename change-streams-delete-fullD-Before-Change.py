from pymongo import MongoClient
from bson.json_util import dumps

# Connect to MongoDB
client = MongoClient("mongodb+srv://user:pass@cluster")  # Replace with your connection string

# Get the database and collection
db = client["migrated"]
collection = db["orders"]

# Watch the collection with fullDocumentBeforeChange set to "required"
change_stream = collection.watch(full_document_before_change="whenAvailable")

# Loop through the change stream
for change in change_stream:
    operation_type = change["operationType"]
    full_document_before = change.get("fullDocumentBeforeChange")  # Access pre-image

    # Process the change based on operation type
    if operation_type == "insert":
        new_document = change["fullDocument"]
        # Process inserted document
    elif operation_type == "update":
        updated_document = change["fullDocument"]
        # Process updated document
    elif operation_type == "delete":
        deleted_document = full_document_before  # Use pre-image for deleted documents
        # Process deleted document
        print(dumps(deleted_document, indent=2))
    else:
        print(f"Unknown operation type: {operation_type}")

# Close the connection
client.close()