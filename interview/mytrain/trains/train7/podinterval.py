'''Дан массив из нулей и единиц. Нужно определить,
какой максимальный по длине подинтервал единиц можно получить,
удалив ровно один элемент массива.

Примеры
[1, 1, 0]
[0, 0, 1, 1, 0, 1, 1, 0]'''

class Solution:
    def search(self, nums: list[int]) -> int:
        left, best, counter = 0, 0, 0

        for right, value in enumerate(nums):
            if value == 0: counter += 1

            while counter > 1:
                if nums[left] == 0:
                    counter -= 1
                left += 1
            best = max(best, right - left)

        return best


if __name__ == '__main__':
    print(Solution().search([1, 1, 0]))
    print(Solution().search([0, 0, 1, 1, 0, 1, 1, 0]))