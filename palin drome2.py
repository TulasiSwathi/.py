def is_palindrome(s):
    # Remove spaces and convert to lowercase
    s = s.replace(" ", "").lower()
    
    # Initialize two pointers
    left, right = 0, len(s) - 1
    
    while left < right:
        # Compare characters from the left and right
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Input a string to check if it's a palindrome
user_input = input("Enter a string: ")

if is_palindrome(user_input):
    print(f"{user_input} is a palindrome.")
else:
    print(f"{user_input} is not a palindrome.")
