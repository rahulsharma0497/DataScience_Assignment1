def is_power_of_two(n):
    if n <= 0:
        return False
    return (n & (n - 1)) == 0

# Example usage
number1 = 16
number2 = 18
print(is_power_of_two(number1))  # Output: True
print(is_power_of_two(number2))  # Output: False
