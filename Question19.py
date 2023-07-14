def remove_vowels(s):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in s if char not in vowels)

# Example usage
string = "Hello, World!"
string_without_vowels = remove_vowels(string)
print(string_without_vowels)  # Output: "Hll, Wrld!"
