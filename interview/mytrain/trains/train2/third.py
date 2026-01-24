class Solution:
    def main(self, nums: list[int], target: int) -> int:
        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] >= target:
                right = mid
            else: left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().main([1,3,3,5,7], 5))
