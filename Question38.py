def find_missing_number(lst):
    n = len(lst) + 1
    total_sum = (n * (n + 1)) // 2
    actual_sum = sum(lst)
    return total_sum - actual_sum

# Example usage
numbers = [1, 2, 3, 5, 6]
missing_number = find_missing_number(numbers)
print(missing_number)  # Output: 4
