from tokenization import tokenize_bulgarian_text
from nltk import bigrams, trigrams
from collections import Counter, defaultdict
import random

with open('IvanVazov1.txt', 'r', encoding='utf-8') as f:
    data = f.read()

# Tokenize text
tokenized_sentences = tokenize_bulgarian_text(data)
print(tokenized_sentences)

# Create a placeholder for model
model = defaultdict(lambda: defaultdict(lambda: 0))

# Count frequency of co-occurance  
for sentence in tokenized_sentences:
    for w1, w2, w3 in trigrams(sentence, pad_right=True, pad_left=True):
        print("Trigram:", (w1, w2, w3))
        model[(w1, w2)][w3] += 1
 
# Transform the counts to probabilities
for w1_w2 in model:
    total_count = float(sum(model[w1_w2].values()))
    for w3 in model[w1_w2]:
        model[w1_w2][w3] /= total_count
print(model)


# starting words
text = ["беше"]
sentence_finished = False
 
print("Starting words:", text)

while not sentence_finished:
    # select a random probability threshold  
    r = random.random()
    accumulator = .0
    for word in model[tuple(text[-2:])].keys():
        print(f"word: {word}, probability: {model[tuple(text[-2:])][word]}, accumulator: {accumulator}")
        accumulator += model[tuple(text[-2:])][word]
        # select words that are above the probability threshold
        if accumulator >= r:
            text.append(word)
            break

    if text[-2:] == [None, None]:
        print("End of sentence.")
        sentence_finished = True
 
print (' '.join([t for t in text if t]))