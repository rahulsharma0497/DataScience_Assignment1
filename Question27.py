def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Example usage
number1 = 48
number2 = 60
gcd_value = gcd(number1, number2)
print(gcd_value)  # Output: 12
