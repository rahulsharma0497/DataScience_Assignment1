def max_subarray_sum(lst):
    max_sum = float('-inf')
    current_sum = 0
    for num in lst:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum

# Example usage
numbers = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
subarray_sum = max_subarray_sum(numbers)
print(subarray_sum)  # Output: 6
