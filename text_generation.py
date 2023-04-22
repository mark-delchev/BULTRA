from transformers import pipeline, set_seed

with open('tokenized_data.txt', 'r', encoding='utf-8') as f:
    text = [line.strip().split() for line in f]
    
text_string = ' '.join([word for sentence in text for word in sentence])
generator = pipeline("text-generation", model="gpt2")
set_seed(42)
generated_text = generator(text_string, max_length=5, num_return_sequences=1)
print(generated_text[0]['generated_text'])
