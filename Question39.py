def sum_of_digits(n):
    return sum(int(digit) for digit in str(n))

# Example usage
number = 12345
digit_sum = sum_of_digits(number)
print(digit_sum)  # Output: 15
