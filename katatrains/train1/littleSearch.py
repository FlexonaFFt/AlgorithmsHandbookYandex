class Solurion:
    def search(self, nums: list[int], x: int) -> int:
        left, right = 0, len(nums)
        while left < right:
            mid = (left + right) // 2

            if nums[mid] < x:
                left = mid + 1
            else: right = mid
        return left if left < len(nums) else -1

if __name__ == '__main__':
    print(Solurion().search([1, 3, 3, 5, 8], 4))
    print(Solurion().search([1, 2, 3], 4))