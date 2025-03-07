import gensim
from gensim.models import Word2Vec
import numpy as np

def preprocess_text(text):
    return text.lower().split()

def train_word2vec(texts, vector_size=100, min_count=1, window=5):
    tokenized_texts = [preprocess_text(text) for text in texts]
    model = Word2Vec(sentences=tokenized_texts, vector_size=vector_size, min_count=min_count, window=window, workers=4)
    return model

def text_to_vector(text, word2vec_model, vector_size=100):
    words = preprocess_text(text)
    vectors = [word2vec_model.wv[word] for word in words if word in word2vec_model.wv]
    return np.mean(vectors, axis=0) if vectors else np.zeros(vector_size)