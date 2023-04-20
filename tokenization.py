import nltk
from nltk.tokenize import word_tokenize
import spacy
from spacy.lang.bg.stop_words import STOP_WORDS as bg_stopwords
import string

filtered_tokens = []

def tokenize_bulgarian_text(text):
    
    # Remove punctuation and lowercase all letters
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    
    # Split the text into individual words or tokens
    tokens = word_tokenize(text)

    # Remove any stop words from the tokenized text
    for i in tokens: 
        if i not in bg_stopwords: 
            filtered_tokens.append(i)


    return filtered_tokens
