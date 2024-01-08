import string

# Define the alphabet
#alphabet = string.ascii_lowercase  # lowercase alphabet
alphabet = "DOG"

# Initialize an empty list to store the combinations
combinations = []

# Nested loops to generate all possible three-letter combinations
for letter1 in alphabet:
    for letter2 in alphabet:
        for letter3 in alphabet:
            word = letter1 + letter2 + letter3
            combinations.append(word)

# Print all the combinations
for word in combinations:
    print(word)
