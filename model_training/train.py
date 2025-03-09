# file: train_model.py

import os
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
data = pd.read_csv('spam_dataset.csv', encoding='latin-1')[['label', 'text']]
data.columns = ['label', 'text']

# Convert labels to binary
data['label'] = data['label'].map({'ham': 0, 'spam': 1})

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    data['text'], data['label'], test_size=0.2, random_state=42
)

# Create pipeline
pipeline = Pipeline([
    ('tfidf', TfidfVectorizer(stop_words='english')),
    ('clf', LogisticRegression(max_iter=1000)),
])

# Train model
pipeline.fit(X_train, y_train)

# Evaluate
y_pred = pipeline.predict(X_test)
print(f"Accuracy: {accuracy_score(y_test, y_pred):.2f}")

# Save model
try:
    os.chdir("../backend/classifier/model")    
    joblib.dump(pipeline, 'spam_classifier.joblib')
    print("Model saved as spam_classifier.joblib")

except Exception as e:
    print(f"Error saving the model : {e}")

finally:
    os.chdir("../../../model_training")