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


# Метод чувака с хабра
class HabrSolution:
    def repr(self, group_start, group_end) -> str:
        if group_start == group_end:
            return str(group_end)
        return f"{group_start}-{group_end}"

    def squeeze(self, numbers: list[int]) -> str:
        if not numbers: return ''
        numbers_, groups = sorted(numbers), []
        last_group_start = None
        last_group_end = None

        for n in numbers_:
            # первая итерация, просто говорим, что группа началась и закончилась
            if last_group_end is None:
                last_group_start = n
                last_group_end = n

            # если предыдущая группа отличается от текущего числа на 1,
            # то это число входит в группу и становится концом текущей группы
            elif last_group_end == n - 1:
                last_group_end = n

            # иначе мы понимаем, что группа закончилась
            # заканчиваем группу и начинаем новую
            else:
                groups.append(self.repr(last_group_start, last_group_end))
                last_group_start = n
                last_group_end = n
        else:
            groups.append(self.repr(last_group_start, last_group_end))
        return ','.join(groups)

# тесты
if __name__ == '__main__':
    solve = Solution()
    habr = HabrSolution()
    case1 = [1,4,5,2,3,9,8,11,0]
    case2, case3 = [1,4,3,2], [1,4]

    print(solve.my_function(case1))
    print(solve.my_function(case2))
    print(solve.my_function(case3))

    print("Habr")
    print(habr.squeeze(case1))
    print(habr.squeeze(case2))
    print(habr.squeeze(case3))
