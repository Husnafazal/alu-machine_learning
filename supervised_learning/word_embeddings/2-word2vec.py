#!/usr/bin/env python3
from gensim.models import Word2Vec
from gensim.utils import simple_preprocess

def word2vec_model(sentences, size=100, min_count=5, window=5, negative=5, cbow=True, iterations=5, seed=0, workers=1):
    sentences = [simple_preprocess(sentence) for sentence in sentences]
    model = Word2Vec(sentences, vector_size=size, min_count=min_count, window=window, sg=0 if cbow else 1,
                     negative=negative, iter=iterations, seed=seed, workers=workers)
    return model

if __name__ == "__main__":
    from gensim.test.utils import common_texts
    model = word2vec_model(common_texts, min_count=1)
    print(model.wv["computer"])
