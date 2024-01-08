'''def reversestring_inalphanumericorder(string):
    letters = ''.join(char for char in string if char.isalpha())
    reversed_letters = letters[::-1]
    print(reversed_letters)
    reversed_letters1 = sorted(reversed_letters)
    result = ''.join(reversed_letters1)
    return result
string = "ez56d"
result = reversestring_inalphanumericorder(string)
print(result)  '''

'''def reversestring_inalphanumericorder(string):
    letters = ''.join(char for char in string if char.isalpha())
    reversed_letters = letters[::-1]
    print(reversed_letters)
    result = []
    num_idx = 0

    for char in string:
        if char.isnumeric():
            result.append(letters[num_idx])
            num_idx += 1
        else:
            result.append(reversed_letters[0])
            reversed_letters = sorted(reversed_letters[1:])
    result = ''.join(reversed_letters)
    return result
string = "ez56d"
result = reversestring_inalphanumericorder(string)
print(result) ''' 



def sorted_reverse_except_numbers(string):
    numbers = ''.join(filter(str.isdigit, string)) #checking only numbers
    letters = ''.join(char for char in string if char.isalpha()) #only alphabets
    reversed_letters = letters[::-1] #reversing alphabets
    result = []
    num_idx = 0

    for char in string:
        if char.isnumeric():
            result.append(numbers[num_idx]) #if number placing in same index value
            num_idx += 1
        else:
            result.append(reversed_letters[0])
            reversed_letters = sorted(reversed_letters[1:])# sorting reversed letters in alphabetical order

    return ''.join(result)

# Example usage
input_value = "ez56d"
result = sorted_reverse_except_numbers(input_value)
print(result)
