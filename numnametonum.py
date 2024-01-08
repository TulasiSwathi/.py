def convert_words_to_numbers(input_str):
    # Define a dictionary to map words to numbers
    word_to_number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
        "zero": "0"
    }

    # Split the input string into words
    words = input_str.split()

    # Initialize an empty string to store the converted number
    converted_number = ""

    # Iterate through each word in the input string
    for word in words:
        # If the word is in the word_to_number dictionary, convert it to the corresponding number
        if word.lower() in word_to_number:
            converted_number += word_to_number[word.lower()]
        else:
            # If the word is not in the dictionary, keep it as is
            converted_number += word

        # Add a space after each word to separate them
        converted_number += " "

    return converted_number.strip()

# Input the string with words
input_string = input("Enter a string with words: ")

# Call the function to convert the words to numbers
converted_string = convert_words_to_numbers(input_string)

# Print the converted string
print("Converted string:", converted_string)
