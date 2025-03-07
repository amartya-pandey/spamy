import pandas as pd
import re

def load_data(filepath='email.csv'):
    df = pd.read_csv(filepath, encoding='latin-1')
    
    # Rename columns for clarity
    df = df.iloc[:, :2]
    df.columns = ['label', 'text']
    
    # Convert labels to binary (1 = spam, 0 = ham)
    df['label'] = df['label'].map({'spam': 1, 'ham': 0})
    
    # Clean text (remove special characters, convert to lowercase)
    df['text'] = df['text'].apply(lambda x: re.sub(r'\W+', ' ', x.lower()))
    
    return df