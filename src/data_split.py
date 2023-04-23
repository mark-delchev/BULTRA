from sklearn.model_selection import train_test_split

# Load the preprocessed data
with open('data.txt', 'r', encoding='utf-8') as f:
    data = f.readlines()

# Split the data into train, validation, and test sets
train_data, test_data = train_test_split(data, test_size=0.1, random_state=42)
train_data, val_data = train_test_split(train_data, test_size=0.2, random_state=42)

# Save the split data to separate files
with open('train_data.txt', 'w', encoding='utf-8') as f:
    f.writelines(train_data)

with open('val_data.txt', 'w', encoding='utf-8') as f:
    f.writelines(val_data)

with open('test_data.txt', 'w', encoding='utf-8') as f:
    f.writelines(test_data)
