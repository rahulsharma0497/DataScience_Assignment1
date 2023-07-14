def is_perfect_number(n):
    if n <= 0:
        return False
    divisors = [i for i in range(1, n) if n % i == 0]
    return sum(divisors) == n

# Example usage
number1 = 6
number2 = 28
print(is_perfect_number(number1))  # Output: True
print(is_perfect_number(number2))  # Output: True
