'''
Дано: piles[i] — кучи бананов, h — число часов.
Коко ест со скоростью k бананов/час (в час выбирает одну кучу).
Найти: минимальное k, чтобы съесть всё за h.
'''


class Searcher:
    def can_finish(self, piles: list[int], h: int, k: int) -> bool:
        hours = 0
        for pile in piles:
            hours += (pile + k - 1) // k
        return hours <= h

    def search(self, piles: list[int], h: int) -> int:
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if self.can_finish(piles, h, mid):
                right = mid
            else: left = mid + 1

        return left


if __name__ == '__main__':
   print(Searcher().search([3,6,7,11], 8))
   print(Searcher().search([30,11,23,4,20], 5))
   print(Searcher().search([30,11,23,4,20], 6))
