class Solution:
    def lower_bound(self, a: list[int], x: int):
        left, right = 0, len(a)

        while left < right:
            mid = (left + right) // 2
            if a[mid] < x:
                left = mid + 1
            else: right = mid
        return left

    def upper_bound(self, a: list[int], x: int):
        left, right = 0, len(a)

        while left < right:
            mid = (left + right) // 2
            if a[mid] <= x:
                left = mid + 1
            else: right = mid
        return left

    def first_last_in_range(self, nums: list[int], L: int, R: int) -> tuple[int, int]:
        n = len(nums)
        first = self.lower_bound(nums, L)
        last = self.upper_bound(nums, R) - 1
        if first >= n or first > last: return -1, -1
        return first, last


if __name__ == '__main__':
    a = [1, 2, 2, 2, 4, 7, 9]
    print(Solution().first_last_in_range(a, 2, 7))  # (1, 5)
    print(Solution().first_last_in_range(a, 3, 6))  # (4, 4)
    print(Solution().first_last_in_range(a, 8, 9))  # (6, 6)
    print(Solution().first_last_in_range(a, 10, 12)) # (-1, -1)