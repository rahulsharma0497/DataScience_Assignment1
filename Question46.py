def first_missing_positive(nums):
    n = len(nums)

    # Step 1: Move all non-positive numbers to the left
    i = 0
    while i < n:
        if 0 < nums[i] <= n and nums[i] != nums[nums[i] - 1]:
            nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
        else:
            i += 1

    # Step 2: Find the first missing positive
    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    # Step 3: If all positive numbers are present, return n + 1
    return n + 1


# Example usage
numbers = [3, 4, -1, 1]
missing_positive = first_missing_positive(numbers)
print(missing_positive)  # Output: 2
