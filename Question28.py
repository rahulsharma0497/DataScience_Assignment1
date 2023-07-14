def square_root(n):
    if n < 0:
        return None
    if n == 0:
        return 0
    x = n
    y = (x + n / x) / 2
    while abs(y - x) >= 1e-5:
        x = y
        y = (x + n / x) / 2
    return x

# Example usage
number = 25
sqrt = square_root(number)
print(sqrt)  # Output: 5.0
