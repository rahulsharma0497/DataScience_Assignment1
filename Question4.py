def count_occurrences(lst):
    occurrence_count = {}
    for item in lst:
        if item in occurrence_count:
            occurrence_count[item] += 1
        else:
            occurrence_count[item] = 1
    return occurrence_count

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 1, 1, 4]
occurrences = count_occurrences(numbers)
print(occurrences)  # Output: {1: 4, 2: 2, 3: 2, 4: 1}
