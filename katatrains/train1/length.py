from typing import List

class Solution:
    def main(self, nums: List[int], S: int) -> int:
        left, curr, best = 0, 0, float('inf')

        for right, value in enumerate(nums):
            curr += value
            while curr >= S:
                best = min(best, right - left + 1)
                curr -= nums[left]
                left += 1

        return 0 if best == float('inf') else best


if __name__ == '__main__':
    print(Solution().main([2, 3, 1, 2, 4, 3], 7))
    print(Solution().main([1, 1, 1], 5))