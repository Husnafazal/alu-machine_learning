#!/usr/bin/env python3
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

def tf_idf(sentences, vocab=None):
    """Generate a TF-IDF embedding matrix from sentences.

    Args:
        sentences (list of str): Sentences to transform into TF-IDF.
        vocab (list of str, optional): Custom vocabulary to use.

    Returns:
        tuple: A tuple containing the embeddings and the feature names.
    """
    vectorizer = TfidfVectorizer(vocabulary=vocab)
    embeddings = vectorizer.fit_transform(sentences).toarray()
    features = vectorizer.get_feature_names_out()
    return embeddings, features

if __name__ == "__main__":
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
    vocab = ["awesome", "learning", "children", "cake", "good", "none", "machine"]
    embeddings, features = tf_idf(sentences, vocab)
    print(embeddings)
    print(features)
