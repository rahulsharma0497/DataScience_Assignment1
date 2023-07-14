def find_largest_element(lst):
    largest = lst[0]
    for num in lst:
        if num > largest:
            largest = num
    return largest

# Example usage
numbers = [5, 10, 2, 8, 3]
largest_number = find_largest_element(numbers)
print(largest_number)  # Output: 10
