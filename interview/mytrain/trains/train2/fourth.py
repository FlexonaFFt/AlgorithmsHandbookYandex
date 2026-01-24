class Solution:
    def lowerBound(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= target:
                right = mid
            else: left = mid + 1
        return left

    def searchRange(self, nums: list[int], target: int) -> list[int]:
        L = self.lowerBound(nums, target)
        if L == len(nums) or nums[L] != target:
            return [-1, -1]

        R = self.lowerBound(nums, target + 1) - 1
        return [L, R]


if __name__ == '__main__':
    print(Solution().searchRange([5,7,7,8,8,10], 8))
