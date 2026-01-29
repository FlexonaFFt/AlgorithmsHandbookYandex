'''
Слияние отрезков:

Вход: [1, 3] [100, 200] [2, 4]
Выход: [1, 4] [100, 200]
'''


class Solve:
    def main(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key=lambda x: (x[0], x[1]))
        cur_start, cur_end = intervals[0]

        output = []
        for start, end in intervals[1:]:
            if start <= cur_end: cur_end = max(cur_end, end)
            else:
                output.append([cur_start, cur_end])
                cur_start, cur_end = start, end

        output.append([cur_start, cur_end])
        return output


if __name__ == '__main__':
    print(Solve().main(intervals=[[1, 3], [100, 200], [2, 4]]))