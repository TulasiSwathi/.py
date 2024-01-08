
def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Base case: if the string is empty or has only one character, it's a palindrome
    if len(s) <= 1:
        return True
    
    # Compare the first and last characters, and recurse on the substring
    if s[0] == s[-1]:
        return is_palindrome(s[1:-1])
    else:
        return False

# Input a string to check if it's a palindrome
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
