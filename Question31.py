def sum_of_even_numbers(lst):
    return sum(num for num in lst if num % 2 == 0)

# Example usage
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum_of_even_numbers(numbers)
print(even_sum)  # Output: 30
