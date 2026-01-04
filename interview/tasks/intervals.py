'''Дан список интов, повторяющихся элементов в списке нет. Нужно преобразовать это множество в строку, сворачивая соседние по числовому ряду числа в диапазоны. Примеры:
[1,4,5,2,3,9,8,11,0] => "0-5,8-9,11"
[1,4,3,2] => "1-4"
[1,4] => "1,4"'''

# Мой метод решения задачи

class Solution:
    def my_function(self, nums: list[int]) -> str:
        nums.sort()
        output: list[str] = []
        start, prev = nums[0], nums[0]

        for num in nums[1:]:
            if num == prev + 1:
                prev = num
            else:
                if start == prev:
                    output.append(str(start))
                else:
                    output.append(f"{start}-{prev}")
                start = num
                prev = num

        if start == prev:
            output.append(str(start))
        else: output.append(f"{start}-{prev}")
        return ','.join(output)


# тесты
if __name__ == '__main__':
    solve = Solution()
    case1 = [1,4,5,2,3,9,8,11,0]
    case2, case3 = [1,4,3,2], [1,4]

    print(solve.my_function(case1))
    print(solve.my_function(case2))
    print(solve.my_function(case3))
