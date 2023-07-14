def find_common_elements(lst1, lst2):
    return list(set(lst1) & set(lst2))

# Example usage
list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
common_elements = find_common_elements(list1, list2)
print(common_elements)  # Output: [4, 5]
