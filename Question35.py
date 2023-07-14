def is_perfect_square(n):
    if n < 0:
        return False
    sqrt = int(n ** 0.5)
    return sqrt * sqrt == n

# Example usage
number1 = 16
number2 = 17
print(is_perfect_square(number1))  # Output: True
print(is_perfect_square(number2))  # Output: False
