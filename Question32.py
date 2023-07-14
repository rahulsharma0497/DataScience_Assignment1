def power(base, exponent):
    if exponent == 0:
        return 1
    elif exponent > 0:
        return base * power(base, exponent - 1)
    else:
        return 1 / power(base, -exponent)

# Example usage
base = 2
exponent = 3
result = power(base, exponent)
print(result)  # Output: 8
