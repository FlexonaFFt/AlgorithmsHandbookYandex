'''
У вас есть набор из N различных цифр (без повторов).
Нужно составить из всех этих цифр число
(переставив их в некотором порядке), которое
делится на M без остатка.

Если таких чисел несколько, требуется вывести
лексикографически наименьшее (т.е. наименьшее по значению).
Если ни одно число не делится на M, выведите No solutions.
'''

from itertools import permutations

class Soltuion:
    def main(self, n: int, m: int, nums: list[int]) -> str:
        nums_sorted, best = sorted(nums), None
        for perm in permutations(nums_sorted):
            if perm[0] == 0: continue

            rem = 0
            for d in perm: rem = (rem * 10 + d) % m
            if rem == 0:
                best = ''.join(map(str, perm))
                break

        return best if best is not None else "No solutions"

    def test(self):
        print(self.main(3, 6, [1, 2, 3]))
        print(self.main(4, 7, [0, 1, 4, 6]))
        print(self.main(3, 37, [0, 5, 8]))


if __name__ == '__main__':
    solve = Soltuion()

    n,m = map(int, input().split())
    nums = list(map(int, input().split()))
    print(solve.main(n, m, nums))
