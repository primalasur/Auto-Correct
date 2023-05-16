# Auto-Correct
AI corrects the word which is nearest to it

In the code below, we first load the English dictionary using the NLTK words corpus. Then, we define a function find_closest_word that takes a misspelled word as input. The function iterates over all the words in the English dictionary and calculates the edit distance between the misspelled word and each word in the dictionary. It keeps track of the minimum distance and the corresponding closest word. Finally, it returns the closest word.
