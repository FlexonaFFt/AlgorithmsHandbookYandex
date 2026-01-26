'''
Дан отсортированный массив и target.
Если target есть, верни индекс.
Если нет — верни индекс, куда его следовало бы вставить,
чтобы сохранить сортировку.
'''

class Solution:
    def main_searcher(self, nums: list[int], target: int):
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else: right = mid - 1

        return left


print(Solution().main_searcher([1, 3, 5, 6], 5))
print(Solution().main_searcher([1, 3, 5, 6], 2))
print(Solution().main_searcher([1, 3, 5, 6], 7))
