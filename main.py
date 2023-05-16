!pip install nltk
import nltk
from nltk.metrics import edit_distance
from nltk.corpus import words

# Load the English dictionary
nltk.download('words')
english_words = set(words.words())

# Function to find the closest word to the misspelled word
def find_closest_word(word):
    min_distance = float('inf')
    closest_word = None

    # Iterate over all the words in the English dictionary
    for english_word in english_words:
        distance = edit_distance(word, english_word)

        # Update the closest word if the current distance is smaller
        if distance < min_distance:
            min_distance = distance
            closest_word = english_word

    return closest_word

# Test the auto-correct tool
misspelled_word = input("Enter a word: ")
closest_word = find_closest_word(misspelled_word)
# print(f"Original word: {misspelled_word}")
print(f"Autocorrected word: {closest_word}")
