#!/usr/bin/env python3

"""
function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """list documents in collection
    return empty list if no doc in collection
    mongo_collection - pymongo collection object
    """
    # check if collection is empty
    docs = []
    collection = mongo_collection.find()
    for doc in collection:
        docs.append(doc)

    return docs