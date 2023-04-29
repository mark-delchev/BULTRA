import random

# Define the order of the Markov chain
order = 2

# Load the dataset
with open('bulgarian_dataset.txt', 'r', encoding='utf-8') as f:
    dataset = f.read()

# Tokenize the dataset
tokens = dataset.split()

# Build the Markov chain model
model = {}
for i in range(len(tokens)-order):
    state = ' '.join(tokens[i:i+order])
    next_word = tokens[i+order]
    if state not in model:
        model[state] = {}
    if next_word not in model[state]:
        model[state][next_word] = 0
    model[state][next_word] += 1

# Generate new text using the Markov chain model
text_length = 10
start_index = random.randint(0, len(tokens)-order)
seed_state = ' '.join(tokens[start_index:start_index+order])
generated_text = seed_state.capitalize()

for i in range(text_length):
    if seed_state not in model:
        break
    next_word = max(model[seed_state], key=model[seed_state].get)
    generated_text += ' ' + next_word
    seed_state = ' '.join(generated_text.split()[-order:])

print(generated_text)
