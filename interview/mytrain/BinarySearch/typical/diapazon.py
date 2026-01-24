class MySolution:
    def lower_bound(self, nums: list[int], target: int) -> int:
        l, r = 0, len(nums)
        while l < r:
            m = (l + r) // 2
            if nums[m] >= target:
                r = m
            else:
                l = m + 1
        return l

    def upper_bound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            median = (left + right) // 2
            if nums[median] > target:
                right = median
            else: left = median + 1
        return left

    def find_interval(self, nums: list[int], target: int) -> tuple[int, int]:
        L = self.lower_bound(nums, target)
        if L == len(nums) or nums[L] != target:
            return (-1, -1)
        R = self.upper_bound(nums, target) - 1
        return (L, R)


if __name__ == '__main__':
    print(MySolution().find_interval([1,3,3,5,8], 5))
