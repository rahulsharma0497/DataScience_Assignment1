def find_smallest_missing_positive(nums):
    n = len(nums)

    # Step 1: Transform the list to contain only positive integers
    for i in range(n):
        if nums[i] <= 0 or nums[i] > n:
            nums[i] = n + 1

    # Step 2: Mark the presence of each positive number
    for i in range(n):
        num = abs(nums[i])
        if num <= n:
            nums[num - 1] = -abs(nums[num - 1])

    # Step 3: Find the first positive number
    for i in range(n):
        if nums[i] > 0:
            return i + 1

    # Step 4: If no positive number found, return n + 1
    return n + 1


# Example usage
numbers = [3, 4, -1, 1]
smallest_missing = find_smallest_missing_positive(numbers)
print(smallest_missing)  # Output: 2
