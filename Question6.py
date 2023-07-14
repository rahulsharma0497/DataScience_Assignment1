def remove_duplicates(lst):
    return list(set(lst))

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 1, 1, 4]
unique_numbers = remove_duplicates(numbers)
print(unique_numbers)  # Output: [1, 2, 3, 4]
