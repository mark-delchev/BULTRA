from tokenization import tokenize_bulgarian_text

with open('data2.txt', 'r', encoding='utf-8') as f:
    text = f.read()


# Tokenize text
tokenized_words = tokenize_bulgarian_text(text)
print(tokenized_words)

# Write tokens to a new file
with open('tokenized_data.txt', 'w', encoding='utf-8') as f:
    for sentence in tokenized_words:
        # Join the words in the sentence into a single string
        # separated by spaces, and write it to the file
        f.write(' '.join(sentence))
        f.write('\n')