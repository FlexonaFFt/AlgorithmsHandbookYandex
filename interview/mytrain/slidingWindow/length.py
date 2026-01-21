class Solution:
    def main(self, nums: list[int], s: int):
        left, best = 0, float('inf')
        current = 0

        for right, val in enumerate(nums):
            current += val
            while current >= s:
                best = min(best, right - left + 1)
                current -= nums[left]
                left += 1

        return 0 if best == float('inf') else best


if __name__ == '__main__':
    print(Solution().main([2,3,1,2,4,3], 7))
