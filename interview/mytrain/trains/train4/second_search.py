'''
Дан массив, где соседние элементы не равны.
Пиком считается элемент, который строго больше
своих соседей. Найди индекс любого пика.
'''

class Solution:
    def search(self, nums: list[int]):
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                left = mid + 1
            else: right = mid
        return left


if __name__ == '__main__':
    print(Solution().search([1, 2, 3, 1]))
    print(Solution().search([1, 2, 1, 3, 5, 6, 4]))
