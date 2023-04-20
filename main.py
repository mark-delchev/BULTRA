from tokenization import tokenize_bulgarian_text
from stemming import stem_bulgarian_words
from numerical_representation import create_numerical_representation

# Load Bulgarian news article
with open('IvanVazov1.txt', 'r', encoding='utf-8') as f:
    text = f.read()


# Tokenize text
tokenized_words = tokenize_bulgarian_text(text)

# Stem words (work in progress)
# stemmed_words = stem_bulgarian_words(tokenized_words)

# Create numerical representation
numerical_representation = create_numerical_representation([tokenized_words])

# Print the numerical representation
print(numerical_representation)
