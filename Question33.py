def remove_duplicates_preserve_order(lst):
    seen = set()
    return [num for num in lst if not (num in seen or seen.add(num))]

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 1, 1, 4]
unique_numbers = remove_duplicates_preserve_order(numbers)
print(unique_numbers)  # Output: [1, 2, 3, 4]
