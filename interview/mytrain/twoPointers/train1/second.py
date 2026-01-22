class Solution:
    def main(self, nums: list[int]):
        slow = 0

        for fast in range(1, len(nums)):
            if nums[fast] >= 0:
                nums[slow] = nums[fast]
                slow += 1

        return nums[:slow]

print(Solution().main([-1, 2, -3, 4, 0]))
