from nltk import ngrams
from collections import defaultdict
import random

# Function to read the corpus from a text file
def load_corpus_from_txt(txt_file):
    with open(txt_file, 'r', encoding='utf-8') as file:
        return file.readlines()

# Function to create n-grams from the corpus
def generate_ngrams(corpus, n):
    ngram_dict = defaultdict(list)
    for sentence in corpus:
        tokens = sentence.lower().split()  # Convert to lowercase
        for ngram in ngrams(tokens, n):
            prefix = ' '.join(ngram[:-1])
            suffix = ngram[-1]
            ngram_dict[prefix].append(suffix)
    return ngram_dict

# User-defined text file
txt_file = 'Pride and Prejudice.txt'

# Load the corpus from the text file
corpus = load_corpus_from_txt(txt_file)

# Generate trigrams from the corpus
n = 3
ngram_dict = generate_ngrams(corpus, n)

# Function to predict the next word using trigrams
def predict_next_word(seed_text, ngram_dict, n):
    tokens = seed_text.lower().split()  # Convert to lowercase
    prefix = ' '.join(tokens[-(n-1):])
    
    possible_next_words = ngram_dict.get(prefix, [])
    if possible_next_words:
        return random.choice(possible_next_words)
    else:
        return None

# User-defined seed text
user_seed_text = input("Enter seed text: ")

# Example usage
predicted_word = predict_next_word(user_seed_text, ngram_dict, n)

if predicted_word:
    print(f'The predicted next word for "{user_seed_text}" is: {predicted_word}')
else:
    print(f'No prediction available for "{user_seed_text}"')
