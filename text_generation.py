import nltk
import random
from nltk.tokenize import word_tokenize
from collections import defaultdict

# Read the file and tokenize its contents into words
with open('IvanVazov2.txt', 'r', encoding='utf-8') as f:
    corpus = f.read()
words = word_tokenize(corpus)

# Create a placeholder for the language model
model = defaultdict(lambda: defaultdict(lambda: 0))

# Count the frequency of co-occurrence of each word
for i in range(len(words)-2):
    w1 = words[i]
    w2 = words[i+1]
    w3 = words[i+2]
    model[(w1, w2)][w3] += 1

# Normalize the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count

# Generate text using the language model
text = ['той', 'беше',]
sentence_finished = False
while not sentence_finished:
    # Select a random probability threshold
    r = random.random()
    accumulator = 0.0

    # Choose the next word based on the probability distribution
    for word in model[tuple(text[-2:])].keys():
        accumulator += model[tuple(text[-2:])][word]
        if accumulator >= r:
            text.append(word)
            break

    # End the sentence if the model generates two consecutive None values
    if text[-2:] == [None, None]:
        sentence_finished = True

# Print the generated text
print(' '.join(text))
