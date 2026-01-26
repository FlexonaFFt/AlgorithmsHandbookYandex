'''
Задача: Дан массив из 0 и 1. Ты можешь заменить не более $K$ нулей на единицы.
Какую максимальную длину последовательности из 1 можно получить?
'''

class Solution:
    def maximum_length(self, nums: list[int], k: int) -> int:
        left, zeros, best = 0, 0, 0

        for right, value in enumerate(nums):
            if value == 0: zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1

            best = max(best, right - left + 1)

        return best


if __name__ == '__main__':
    print(Solution().maximum_length([0,0,1,1,0,0,1,1,1], 2))
