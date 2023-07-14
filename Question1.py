def reverse_string(s):
    reversed_string = ""
    for char in s:
        reversed_string = char + reversed_string
    return reversed_string

# Example usage
string = "Hello, World!"
reversed_string = reverse_string(string)
print(reversed_string)  # Output: "!dlroW ,olleH"