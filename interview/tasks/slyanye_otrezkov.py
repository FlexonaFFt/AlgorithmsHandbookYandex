'''
Слияние отрезков:

Вход: [1, 3] [100, 200] [2, 4]
Выход: [1, 4] [100, 200]
'''

class Solution:
    def main(self, ranges: list[list[int]]) -> list[list[int]]:
        if not ranges: return []
        result, last_range = [], []

        for rng in sorted(ranges):
            if not last_range:
                last_range = rng
                continue

            if rng[0] <= last_range[1]:
                last_range = (last_range[0], max(rng[1], last_range[1]))

            else:
                result.append(last_range)
                last_range = rng

        else: result.append(last_range)
        return result

    def myprobe(self, ranges: list[list[int]]):
        if not ranges: return []
        output, current = [], None

        for range in sorted(ranges):
            if not current:
                current = range
                continue

            if range[0] <= current[1]:
                current = (current[0], max(range[1], current[1]))
            else:
                output.append(current)
                current = range

        else: output.append(current)
        return output

if __name__ == '__main__':
    solve = Solution()
    print(solve.main([[1, 3], [100, 200], [2, 4]]))
    print(solve.myprobe([[1, 3], [100, 200], [2, 4]]))
