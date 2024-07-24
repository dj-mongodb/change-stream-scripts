from pymongo import MongoClient
from pymongo.errors import PyMongoError

# MongoDB connection URI
uri = "mongodb+srv://user:pass@cluster"  # Update this with your MongoDB connection string
client = MongoClient(uri)

# Database and collection
db = client['user']  # Replace with your database name
collection = db['col']  # Replace with your collection name

# Define the change stream pipeline to watch for replace operations
pipeline = [
    {
        '$match': {
            'operationType': 'replace'
        }
    }
]

try:
    # Start the change stream
    with collection.watch(pipeline) as stream:
        print("Watching for replace operations...")
        for change in stream:
            print("Replace operation detected:")
            print(change)

except PyMongoError as e:
    print(f"An error occurred: {e}")

finally:
    # Close the MongoDB connection
    client.close()
