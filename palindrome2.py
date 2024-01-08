def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Compare the original string with its reverse
    return s == s[::-1]

# Input a string to check if it's a palindrome
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
