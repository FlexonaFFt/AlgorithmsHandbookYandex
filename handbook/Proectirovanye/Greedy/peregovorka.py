'''
Задано n интервалов. Требуется найти максимальное
количество взаимно непересекающихся интервалов.

Два интервала пересекаются, если они имеют
хотя бы одну общую точку.
'''

class Solution:
    def input_function(self):
        n = int(input())
        function_list = []
        for _ in range(n):
            s, e = map(int, input().split())
            function_list.append([s, e])
        return function_list

    def main_function(self, intervals: list[list[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: (x[1], x[0]))
        counter, last_end = 0, None

        for s, e in intervals:
            if last_end is None or s > last_end:
                counter += 1
                last_end = e

        return counter

    def main(self):
        inpt = self.input_function()
        print(self.main_function(inpt))


if __name__ == '__main__':
    Solution().main()
