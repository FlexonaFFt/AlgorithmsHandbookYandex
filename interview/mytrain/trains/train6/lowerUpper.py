class lowerUpper:
    def find(self, nums: list[int], x: int):
        return self.upper_bound(nums, x) - self.lower_bound(nums, x)

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


if __name__ == "__main__":
    a = [1, 2, 2, 2, 4, 7]
    print(lowerUpper().find(a, 2))  # 3
    print(lowerUpper().find(a, 3))  # 0