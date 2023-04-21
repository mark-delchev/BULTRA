from tokenization import tokenize_bulgarian_text
from numerical_representation import create_numerical_representation

# Load Bulgarian news article
with open('IvanVazov2.txt', 'r', encoding='utf-8') as f:
    text = f.read()


# Tokenize text
tokenized_words = tokenize_bulgarian_text(text)

# Create numerical representation
numerical_representation = create_numerical_representation([tokenized_words])

# Print the numerical representation
print(dict(sorted(numerical_representation.items(), key=lambda x: (-x[1], x[0]))))
