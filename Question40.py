def is_valid_palindrome_case_sensitive(s):
    return s == s[::-1]

# Example usage
string1 = "Madam"
string2 = "Racecar"
print(is_valid_palindrome_case_sensitive(string1))  # Output: False
print(is_valid_palindrome_case_sensitive(string2))  # Output: True
