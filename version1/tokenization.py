import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
import string
from spacy.lang.bg.stop_words import STOP_WORDS as bg_stopwords


def tokenize_bulgarian_text(text):
    extra_stopwords = {"—", "“", "„", "не", "та", "па"}
    bg_stopwords.update(extra_stopwords)
    
    # Split the text into individual sentences
    sentences = sent_tokenize(text)

    # Tokenize the text in batches of 1000 sentences
    batch_size = 1000
    filtered_tokens = []
    for i in range(0, len(sentences), batch_size):
        batch = sentences[i:i+batch_size]
        filtered_batch = []
        for sentence in batch:
            # Remove punctuation and lowercase all letters
            sentence = sentence.translate(str.maketrans('', '', string.punctuation))
            sentence = sentence.lower()
        
            # Split the sentence into individual words or tokens
            tokens = word_tokenize(sentence)
        
            # Remove any stop words from the tokenized text
            filtered_sentence = [word for word in tokens if word not in bg_stopwords]
            filtered_batch.append(filtered_sentence)
        filtered_tokens.extend(filtered_batch)

    return filtered_tokens
