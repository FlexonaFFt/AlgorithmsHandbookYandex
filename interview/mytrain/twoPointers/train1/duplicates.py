class Solution:
    def main(self, nums: list[int]):
        slow = 1

        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1

        return nums[:slow]


if __name__ == '__main__':
    print(Solution().main([1, 1, 1, 5, 5]))
