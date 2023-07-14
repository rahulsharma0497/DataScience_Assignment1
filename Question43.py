def count_occurrences(lst, target):
    return lst.count(target)

# Example usage
numbers = [1, 2, 3, 4, 2, 1, 2, 2]
target = 2
occurrences = count_occurrences(numbers, target)
print(occurrences)  # Output: 4
