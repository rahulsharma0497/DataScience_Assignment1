def find_median(lst):
    sorted_list = sorted(lst)
    n = len(sorted_list)
    if n % 2 == 0:
        return (sorted_list[n//2-1] + sorted_list[n//2]) / 2
    else:
        return sorted_list[n//2]

# Example usage
numbers = [5, 2, 7, 1, 9, 4, 3]
median = find_median(numbers)
print(median)  # Output: 4
