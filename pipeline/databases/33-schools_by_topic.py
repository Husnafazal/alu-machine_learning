#!/usr/bin/env python3

"""
function that returns the list of
school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """return list of school with specific topics
    mongo_collection - pymongo collection object
    topic - topic searched
    """
    schools = []
    collections = mongo_collection.find({'topics': topic})
    for doc in collections:
        schools.append(doc)

    return schools