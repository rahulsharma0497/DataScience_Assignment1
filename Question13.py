def permutations(string):
    if len(string) <= 1:
        return [string]
    perms = []
    for i in range(len(string)):
        char = string[i]
        remaining_chars = string[:i] + string[i+1:]
        for perm in permutations(remaining_chars):
            perms.append(char + perm)
    return perms

# Example usage
string = "abc"
all_perms = permutations(string)
print(all_perms)  # Output: ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
