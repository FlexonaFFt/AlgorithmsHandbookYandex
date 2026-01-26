class Solution:
    def maximum(self, nums: list[int], k: int) -> int:
        current_window = sum(nums[:k])
        maximum = current_window

        for right in range(k, len(nums)):
            current_window += nums[right] - nums[right - k]
            if maximum < current_window:
                maximum = current_window
        return maximum

if __name__ == '__main__':
    print(Solution().maximum([2, 1, 5, 1, 3, 2], 3))
