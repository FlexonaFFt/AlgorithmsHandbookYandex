class Solution:
    def find_the_mid(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        best = window

        for right in range(k, len(nums)):
            window += nums[right] - nums[right - k]
            best = max(best, window)

        return best / k


if __name__ == '__main__':
    print(Solution().find_the_mid([1,12,-5,-6,50,3], 4))
