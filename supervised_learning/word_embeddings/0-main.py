#!/usr/bin/env python3

# Import the bag_of_words function from your implementation file
from typing import Tuple
from numpy import ndarray
bag_of_words = __import__('0-bag_of_words').bag_of_words

# Sample sentences
sentences = [
    "Holberton school is Awesome!",
    "Machine learning is awesome",
    "NLP is the future!",
    "The children are our future",
    "Our children's children are our grandchildren",
    "The cake was not very good",
    "No one said that the cake was not very good",
    "Life is beautiful"
]

# Call the bag_of_words function to get E and F
E: ndarray
F: list[str]
E, F = bag_of_words(sentences)

# Print the matrices E and F
print("Matrix E:")
print(E)
print("\nList F:")
print(F)
