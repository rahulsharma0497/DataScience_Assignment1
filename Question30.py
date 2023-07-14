def find_minimum(lst):
    left = 0
    right = len(lst) - 1
    while left < right:
        mid = (left + right) // 2
        if lst[mid] > lst[right]:
            left = mid + 1
        else:
            right = mid
    return lst[left]

# Example usage
numbers = [4, 5, 6, 7, 0, 1, 2]
minimum = find_minimum(numbers)
print(minimum)  # Output: 0
