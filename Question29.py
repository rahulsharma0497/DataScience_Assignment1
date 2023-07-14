import re

def is_valid_palindrome(s):
    s = re.sub(r'[^a-zA-Z0-9]', '', s.lower())
    return s == s[::-1]

# Example usage
string1 = "A man, a plan, a canal: Panama"
string2 = "race a car"
print(is_valid_palindrome(string1))  # Output: True
print(is_valid_palindrome(string2))  # Output: False
