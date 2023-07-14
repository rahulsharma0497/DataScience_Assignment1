def remove_duplicates(s):
    return ''.join(set(s))

# Example usage
string = "hello"
string_without_duplicates = remove_duplicates(string)
print(string_without_duplicates)  # Output: "helo"
