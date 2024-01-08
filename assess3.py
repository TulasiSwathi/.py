import string
from itertools import permutations
name= "DOG" # assigning word to variable
combinations = [] #empty list
for perm in permutations(name, 3):# for checking all possibilities using permutations
    word = ''.join(perm)
    combinations.append(word)
for word in combinations: # Printing all the unique combinations
    print(word)


