class Solution:
    def main(self, intervals: list[list[int]]) -> int:
        if not intervals: return 0
        intervals.sort(key=lambda x: x[1])
        points, current_poin = 0, None

        for l, r in intervals:
            if current_poin is None or current_poin < l:
                current_poin = r
                points += 1

        return points


solve = Solution()
print(solve.main([[1, 3], [2, 5], [3, 6], [7, 9]]))
