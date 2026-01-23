class Solution:
    def main(self, nums: list[int]) -> list[int]:
        if not nums: return 0

        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return nums[:slow]

print(Solution().main([0,0,1,1,2,2,3]))
