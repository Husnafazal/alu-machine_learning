// Insert Sample Users
db.users.insertMany([
    { name: "Jane Doe", email: "jane@example.com", password: "password123" },
    { name: "John Smith", email: "john@example.com", password: "securePass456" }
  ]);
  
  // Assume the use of actual ObjectIds from the users collection for userId fields below
  // Insert Sample Products
  db.products.insertMany([
    { name: "Laptop Pro", description: "High-end gaming laptop", price: 1500, userId: ObjectId("...") },
    { name: "Smartphone X", description: "Latest smartphone model", price: 1000, userId: ObjectId("...") }
  ]);
  
  // Insert Sample Transactions
  db.transactions.insertMany([
    { productId: ObjectId("..."), buyerId: ObjectId("..."), date: new ISODate("2023-10-01"), quantity: 1 },
    { productId: ObjectId("..."), buyerId: ObjectId("..."), date: new ISODate("2023-10-02"), quantity: 2 }
  ]);
  
  print("Sample data insertion complete.");
  