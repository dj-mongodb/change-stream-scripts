1. Use DB
2. db.runCommand( { collMod: "orders", changeStreamPreAndPostImages: { enabled: true} } )
3. Not supported on a TS collection
3. In the watch set `full_document_before_change="whenAvailable"`
4. Delete a document - It responds back with the doc
5. Set TTL - db.orders.createIndex( { "orderDate": 1 }, { expireAfterSeconds: 1 } )
