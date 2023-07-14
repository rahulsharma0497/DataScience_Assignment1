def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))

# Example usage
numbers1 = [1, 2, 3, 4, 5]
numbers2 = [5, 2, 7, 1, 9, 4, 3]
print(is_sorted(numbers1))  # Output: True
print(is_sorted(numbers2))  # Output: False
