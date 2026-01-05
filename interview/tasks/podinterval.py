'''Дан массив из нулей и единиц. Нужно определить,
какой максимальный по длине подинтервал единиц можно получить,
удалив ровно один элемент массива.

Примеры
[1, 1, 0]
[0, 0, 1, 1, 0, 1, 1, 0]'''

class Solution:
    def podinterval(self, nums: list[int]) -> int:
        left, zeros, best = 0, 0, 0
        for right in range(len(nums)):
            if nums[right] == 0:
                zeros += 1
            while zeros > 1:
                if nums[left] == 0: zeros -= 1
                left += 1
            best = max(best, (right - left + 1) - 1)
        return best

if __name__ == '__main__':
    solve = Solution()
    case1 = [1, 1, 0]
    case2 = [0, 0, 1, 1, 0, 1, 1, 0]
    print(solve.podinterval(case1))
    print(solve.podinterval(case2))
