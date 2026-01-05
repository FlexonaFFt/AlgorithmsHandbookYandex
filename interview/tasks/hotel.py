'''
Даны даты заезда и отъезда каждого гостя.
Для каждого гостя дата заезда строго раньше даты отъезда
(то есть каждый гость останавливается хотя бы на одну ночь).
В пределах одного дня считается, что сначала старые гости выезжают, а затем въезжают новые.
Найти максимальное число постояльцев, которые одновременно проживали в гостинице
(считаем, что измерение количества постояльцев происходит в конце дня).

sample = [ (1, 2), (1, 3), (2, 4), (2, 3), ]
'''

# Мое решение
class Solution:
    def main(self, stays) -> int:
        events = []
        for day_in, day_out in stays:
            events.append((day_in, +1))
            events.append((day_out, -1))

        # сортируем, сначала выезда, потом въезды
        events.sort(key=lambda x: (x[0], x[1]))
        current, best, i = 0, 0, 0
        while i < len(events):
            day = events[i][0]
            while i < len(events) and events[i][0] == day:
                current += events[i][1]
                i += 1
            best = max(best, current)

        return best

# Решение парня с хабра
from collections import defaultdict
from os import terminal_size

class HabrSolution:
    def main(self, guests: list[tuple]) -> int:
        res, current = 0, 0
        # для каждого дня посчитаем, сколько приехало и сколько отъехало
        arriving = defaultdict(int)
        leaving = defaultdict(int)

        for guest in guests:
            arriving[guest[0]] += 1
            leaving[guest[1]] += 1

        # едем по дням в порядке увеличения, добавлем приехавших и убавляем уехавших,
        # считаем сколько стало
        for day in sorted(set(arriving.keys()).union(set(leaving.keys()))):
            current -= leaving[day]
            current += arriving[day]
            if current > res: res = current

        return res


if __name__ == '__main__':
    solve, habr = Solution(), HabrSolution()
    test_case = [(1, 2),(1, 3),(2, 4),(2, 3)]
    print(solve.main(stays=test_case))
    print(habr.main(test_case))
