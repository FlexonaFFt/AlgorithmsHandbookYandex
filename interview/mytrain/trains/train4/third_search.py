def splitArray(nums, m):
    def canSplit(max_sum):
        current_sum, count = 0, 1
        for num in nums:
            if current_sum + num > max_sum:
                count += 1
                current_sum = num
                if count > m: return False
            else: current_sum += num
        return True


    left, right = max(nums), sum(nums)
    result = right

    while left <= right:
        mid = (left + right) // 2
        if canSplit(mid):
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result


if __name__ == '__main__':
    print(splitArray([7, 2, 5, 10, 8], 2))
    print(splitArray([1, 2, 3, 4, 5], 5))
