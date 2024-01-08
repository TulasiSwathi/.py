'''import string
from itertools import permutations

name= input("enter any word") # assigning word to variable

combinations = [] #empty list


for perm in permutations(name):# for checking all possibilities using permutations
    word = ''.join(perm)
    combinations.append(word)



for word in combinations: # Printing all the unique combinations
    print(word)
'''
def generate_word_combinations(input_text, dictionary):
    def is_proper_word(word):
        return word in dictionary

    def find_word_combinations(current_word, remaining_text):
        if not remaining_text:
            if is_proper_word(current_word):
                valid_word_combinations.append(current_word)
            return

        for i in range(1, len(remaining_text) + 1):
            prefix = remaining_text[:i]
            rest = remaining_text[i:]
            if is_proper_word(prefix):
                find_word_combinations(current_word + prefix, rest)
            find_word_combinations(current_word, rest)

    input_text = input_text.upper()  # Convert the input text to uppercase for case-insensitive matching
    valid_word_combinations = []
    find_word_combinations("", input_text)
    
    return valid_word_combinations

# Example usage:
valid_words = set(["GO", "DOG", "ODD"])  # Sample dictionary of valid words
input_text = "GOD"
combinations = generate_word_combinations(input_text, valid_words)
print(combinations)  
