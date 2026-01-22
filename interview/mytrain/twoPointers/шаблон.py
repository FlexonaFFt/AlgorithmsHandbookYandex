def two_pointers(nums):
    slow = 0

    for fast in range(len(nums)):
        if condition(nums[fast]):
            nums[slow] = nums[fast]
            slow += 1

    return nums[:slow]
