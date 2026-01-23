class Solution:
    def main(self, nums: list[int], k: int) -> int:
        window = sum(nums[:k])
        best = window

        for right in range(k, len(nums)):
            window += nums[right] - nums[right - k]
            if window > best: best = window
        return best


if __name__ == '__main__':
    print(Solution().main([2,1,5,1,3,2], 3))
    print(Solution().main([0, 0, 0, 0], 0))
    print(Solution().main([-1,-2,-3,-4], 2))
    print(Solution().main([1,2,3,4,5], 5))
