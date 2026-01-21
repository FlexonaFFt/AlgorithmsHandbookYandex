class Solution:
    def main(self, nums: list[int], S: int):
        left, best, current = 0, 0, 0

        for right, val in enumerate(nums):
            current += val
            while current > S:
               current -= nums[left]
               left += 1

            best = max(best, right - left + 1)
        return best


if __name__ == '__main__':
    print(Solution().main([2,1,1,1,3], 4))
