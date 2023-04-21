import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from spacy.lang.bg.stop_words import STOP_WORDS as bg_stopwords



def tokenize_bulgarian_text(text):
    extra_stopwords = {"—", "“", "„", "не", "та", "па"}
    bg_stopwords.update(extra_stopwords)
    # Remove punctuation and lowercase all letters
    text = text.translate(str.maketrans('', '', string.punctuation))
    text = text.lower()
    
    # Split the text into individual sentences
    sentences = sent_tokenize(text)

    # Tokenize and filter each sentence
    filtered_tokens = []
    for sentence in sentences:
        # Split the sentence into individual words or tokens
        tokens = word_tokenize(sentence)
        # Remove any stop words from the tokenized text
        filtered_sentence = [word for word in tokens if word not in bg_stopwords]
        filtered_tokens.append(filtered_sentence)

    return filtered_tokens

