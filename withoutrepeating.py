import string
from itertools import permutations

# Define the alphabet
#alphabet = string.ascii_lowercase  # lowercase alphabet
alphabet= "DOG"

# Initialize an empty list to store the combinations
combinations = []

# Generate all unique three-letter permutations
for perm in permutations(alphabet, 3):
    word = ''.join(perm)
    combinations.append(word)

# Print all the unique combinations
for word in combinations:
    print(word)
#In this code, we use the permutations function from the itertools module to generate all unique three-letter permutations of the alphabet. This ensures that no letter is repeated in a single word. The resulting unique combinations are stored in the combinations list and then printed.





