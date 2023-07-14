def find_second_largest(lst):
    largest = float('-inf')
    second_largest = float('-inf')
    for num in lst:
        if num > largest:
            second_largest = largest
            largest = num
        elif num > second_largest and num < largest:
            second_largest = num
    return second_largest

# Example usage
numbers = [5, 10, 2, 8, 3]
second_largest = find_second_largest(numbers)
print(second_largest)  # Output: 8
