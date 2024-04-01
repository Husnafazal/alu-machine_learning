// Create Users Collection with Unique Email Index
db.createCollection("users");
db.users.createIndex({ email: 1 }, { unique: true });

// Create Products Collection
db.createCollection("products");

// Create Transactions Collection
db.createCollection("transactions");

print("Database setup complete.");
