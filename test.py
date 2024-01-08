import string
def convert_words_to_numbers(mobilenumber):
    # assigning numbernames to numbers in a dictionary
    word_to_number = {
        'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9', 'Z': '9'
    }

    words = mobilenumber.split() #string to words

    convertednumber = "" #an empty string for numbers after conversion

   
    for word in words: #checking each word in the input string
        
        if word.lower() in word_to_number: # If the word is in assigned dictionary, it will convert to that number

            convertednumber += word_to_number[word.lower()]
        else:
           
            convertednumber += word  # If the word is not in the dictionary, keep it without any change
        convertednumber += " "  # Add a space after each word to separate them

    return convertednumber.strip()
mobilenumber = input("Enter a string with mobile number in words: ") # Input the string with words

converted_string = convert_words_to_numbers(mobilenumber) # Call the function to convert the words to numbers

print("Converted string:", converted_string)# Print the converted string

'''try:
    phone_number_with_letters = "800888TEST"
    converted_string = convert_phone_number(phone_number_with_letters)
    print(f"Converted Phone Number: {converted_string}")
except ValueError as e:
    print(f"Error: {e}")'''