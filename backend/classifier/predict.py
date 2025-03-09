# file: predict.py

import joblib

# Load the saved model
model = joblib.load('classifier/model/spam_classifier.joblib')

def classify_email(message):
    prediction = model.predict([message])[0]
    return 'spam' if prediction == 1 else 'ham'
