import joblib
import numpy as np
from gensim.models import Word2Vec
from classifier.preprocess import text_to_vector

# Load trained models
word2vec_model = Word2Vec.load('backend/classifier/model/word2vec.model')
spam_classifier = joblib.load('backend/classifier/model/spam_classifier.pkl')

def classify_email(text):
    vector = text_to_vector(text, word2vec_model).reshape(1, -1)
    prediction = spam_classifier.predict(vector)[0]
    return "Spam" if prediction == 1 else "Ham"