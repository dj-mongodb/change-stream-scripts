from pymongo import MongoClient
from pymongo.errors import PyMongoError
from bson.json_util import dumps

def main():
    # MongoDB connection URI
    uri = "mongodb+srv://user:pass@cluster"  # Update this with your MongoDB connection string
    client = MongoClient(uri)

    # Database and collection
    db = client['meanStackExample']  # Replace with your database name
    collection = db['employees']  # Replace with your collection name

    # Change stream to listen for insert operations
    try:
        with collection.watch([{'$match': {'operationType': 'insert'}}]) as stream:
            print("Listening for new inserts...")
            for change in stream:
                print("New document inserted:")
                print(dumps(change['fullDocument'], indent=2))

    except PyMongoError as e:
        print(f"An error occurred: {e}")

    finally:
        client.close()

if __name__ == "__main__":
    main()
