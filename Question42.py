def longest_palindrome_substring(s):
    n = len(s)
    longest_palindrome = ""

    # Helper function to expand around center
    def expand_around_center(left, right):
        while left >= 0 and right < n and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    for i in range(n):
        palindrome_odd = expand_around_center(i, i)
        palindrome_even = expand_around_center(i, i + 1)
        longest_palindrome = max(longest_palindrome, palindrome_odd, palindrome_even, key=len)

    return longest_palindrome


# Example usage
string = "babad"
longest_palindrome = longest_palindrome_substring(string)
print(longest_palindrome)  # Output: "bab"
