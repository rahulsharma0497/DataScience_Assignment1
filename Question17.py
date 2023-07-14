def find_intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
intersection = find_intersection(list1, list2)
print(intersection)  # Output: [4, 5]
