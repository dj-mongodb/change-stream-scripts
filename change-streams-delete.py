from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.json_util import dumps

def main():
    # MongoDB connection URI
    uri = "mongodb+srv://user:pas@cluster"  # Update this with your MongoDB connection string
    client = MongoClient(uri)

    # Database and collection
    db = client['user']  # Replace with your database name
    collection = db['col']  # Replace with your collection name

    # Change stream to listen for delete operations
    try:
        with collection.watch([{'$match': {'operationType': 'delete'}}], full_document_before_change="required") as stream:
            print("Listening for delete operations...")
            for change in stream:
                print("Document deleted:")
                print(dumps(change, indent=2))

    except PyMongoError as e:
        print(f"An error occurred: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()
