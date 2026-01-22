class Solution:
    def main(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        best = window / k

        for right in range(k, len(nums)):
            window += nums[right] - nums[right - k]
            best = max(best, window / k)

        return best


if __name__ == '__main__':
    print(Solution().main([1,12,-5,-6,50,3], 4))
    print(Solution().main([-1,-2,-3,-4], 2))
    print(Solution().main([1,2,3,4,5], 5))
