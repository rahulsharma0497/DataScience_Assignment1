def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)

# Example usage
string1 = "listen"
string2 = "silent"
print(are_anagrams(string1, string2))  # Output: True
