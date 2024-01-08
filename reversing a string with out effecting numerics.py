def reverse_alphabets(input_str):
    alphabet_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reversed_str = ''

    for char in input_str:
        if char in alphabet_chars:
            reversed_str += char
        else:
            reversed_str = char + reversed_str

    return reversed_str

# Example usage
input_value = "a1b2c3d4e5"
result = reverse_alphabets(input_value)
print(result)
