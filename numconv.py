def convert_mobile_number(input_str):
    # Define a dictionary to map letters to their corresponding digits
    letter_to_digit = {
        'A': '2', 'B': '2', 'C': '2',
        'D': '3', 'E': '3', 'F': '3',
        'G': '4', 'H': '4', 'I': '4',
        'J': '5', 'K': '5', 'L': '5',
        'M': '6', 'N': '6', 'O': '6',
        'P': '7', 'Q': '7', 'R': '7', 'S': '7',
        'T': '8', 'U': '8', 'V': '8',
        'W': '9', 'X': '9', 'Y': '9', 'Z': '9',
    }

    # Initialize an empty string to store the converted mobile number
    converted_number = ""

    # Iterate through each character in the input string
    for char in input_str:
        if char.isalpha():
            # If the character is a letter, convert it to the corresponding digit
            # using the letter_to_digit dictionary
            digit = letter_to_digit.get(char.upper(), char)
            converted_number += digit
        else:
            # If the character is not a letter, keep it as is
            converted_number += char

    return converted_number

# Input the mobile number
input_number = input("Enter a mobile number (with letters): ")

# Call the function to convert the mobile number
converted_number = convert_mobile_number(input_number)

# Print the converted mobile number
print("Converted mobile number:", converted_number)
