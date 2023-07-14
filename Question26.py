from collections import Counter

def find_mode(lst):
    counter = Counter(lst)
    max_count = max(counter.values())
    modes = [num for num, count in counter.items() if count == max_count]
    return modes

# Example usage
numbers = [1, 2, 3, 2, 1, 3, 1, 1, 4]
modes = find_mode(numbers)
print(modes)  # Output: [1]
