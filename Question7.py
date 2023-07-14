def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result

# Example usage
number = 5
factorial_value = factorial(number)
print(factorial_value)  # Output: 120
