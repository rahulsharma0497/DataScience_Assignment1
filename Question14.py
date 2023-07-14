def fibonacci(n):
    fib_seq = [0, 1]
    for i in range(2, n):
        fib_seq.append(fib_seq[i-1] + fib_seq[i-2])
    return fib_seq

# Example usage
terms = 8
fib_sequence = fibonacci(terms)
print(fib_sequence)  # Output: [0, 1, 1, 2, 3, 5, 8, 13]
