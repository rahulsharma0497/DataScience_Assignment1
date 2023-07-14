def longest_common_prefix(strings):
    if not strings:
        return ""
    shortest = min(strings, key=len)
    for i, char in enumerate(shortest):
        if any(string[i] != char for string in strings):
            return shortest[:i]
    return shortest

# Example usage
words = ["flower", "flow", "flight"]
common_prefix = longest_common_prefix(words)
print(common_prefix)  # Output: "fl"
