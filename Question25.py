def merge_sorted_lists(lst1, lst2):
    merged_list = []
    i = 0
    j = 0
    while i < len(lst1) and j < len(lst2):
        if lst1[i] <= lst2[j]:
            merged_list.append(lst1[i])
            i += 1
        else:
            merged_list.append(lst2[j])
            j += 1
    while i < len(lst1):
        merged_list.append(lst1[i])
        i += 1
    while j < len(lst2):
        merged_list.append(lst2[j])
        j += 1
    return merged_list

# Example usage
list1 = [1, 3, 5, 7]
list2 = [2, 4, 6, 8]
merged_list = merge_sorted_lists(list1, list2)
print(merged_list)  # Output: [1, 2, 3, 4, 5, 6, 7, 8]
