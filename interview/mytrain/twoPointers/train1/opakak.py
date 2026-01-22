class Solution:
    def main(self, nums: list[int]):
        i = 0

        for j in range(len(nums)):
            if nums[j] % 2 != 0:
                nums[i] = nums[j]
                i += 1
        return nums[:i]

print(Solution().main([1, 2, 3, 4, 5]))
