// Query to find all products listed by a specific user
// Replace `...` with the actual userId
db.products.find({ userId: ObjectId("...") });

// Query to find the total amount spent by a specific user
// Replace `...` with the actual buyerId
db.transactions.aggregate([
  { $match: { buyerId: ObjectId("...") } },
  {
    $lookup: {
      from: "products",
      localField: "productId",
      foreignField: "_id",
      as: "productDetails"
    }
  },
  { $unwind: "$productDetails" },
  {
    $group: {
      _id: "$buyerId",
      totalSpent: { $sum: { $multiply: ["$quantity", "$productDetails.price"] } }
    }
  }
]);

// Query to find the top 5 most popular products
db.transactions.aggregate([
  { $group: { _id: "$productId", transactionCount: { $sum: 1 } } },
  { $sort: { transactionCount: -1 } },
  { $limit: 5 },
  {
    $lookup: {
      from: "products",
      localField: "_id",
      foreignField: "_id",
      as: "productInfo"
    }
  },
  { $unwind: "$productInfo" }
]);

print("Queries executed.");
