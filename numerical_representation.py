from collections import defaultdict

def create_numerical_representation(corpus):
    # Initialize an empty dictionary
    dictionary = defaultdict(int)

    # Iterate over each document in the corpus
    for doc in corpus:
        # Iterate over each sentence in the document
        for sentence in doc:
            # Iterate over each token in the sentence
            for token in sentence:
                # Increment the count for the current token in the dictionary
                dictionary[token] += 1

    return dictionary

