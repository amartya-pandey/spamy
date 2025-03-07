from sklearn.naive_bayes import GaussianNB
import numpy as np
import joblib
from classifier.dataset_loader import load_data
from classifier.preprocess import train_word2vec, text_to_vector

# Load dataset
df = load_data('data/email.csv')

# Train Word2Vec model
word2vec_model = train_word2vec(df['text'])
word2vec_model.save('classifier/model/word2vec.model')

# Convert text to vectors
X = np.array([text_to_vector(text, word2vec_model) for text in df['text']])
y = df['label'].values

# Train Naive Bayes classifier
nb_model = GaussianNB()
nb_model.fit(X, y)

# Save trained model
joblib.dump(nb_model, 'classifier/model/spam_classifier.pkl')
print("Model training complete and saved!")