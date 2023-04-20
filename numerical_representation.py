from collections import defaultdict

def create_numerical_representation(corpus):
    # Initialize an empty dictionary
    dictionary = defaultdict(int)

    # Iterate over each document in the corpus
    for doc in corpus:
        # Iterate over each token in the document
        for token in doc:
            # Increment the count for the current token in the dictionary
            dictionary[token] += 1

    return dictionary
