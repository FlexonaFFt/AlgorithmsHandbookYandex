class Solution:
    def podstroka_all_ones(self, nums: list[int], k: int) -> int:
        left, current_zeros, best = 0, 0, 0

        for right, value in enumerate(nums):
            if value == 0:
                current_zeros += 1

            while current_zeros > k:
                if nums[left] == 0:
                    current_zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == '__main__':
    print(Solution().podstroka_all_ones([1,1,1,0,0,0,1,1,1,1,0], 2))
    print(Solution().podstroka_all_ones([0, 0, 0, 1], 4))