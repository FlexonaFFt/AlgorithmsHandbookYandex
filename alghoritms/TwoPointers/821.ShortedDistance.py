from typing import List

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        dist = [10**9] * len(s)
        prev_left = -10**9
        for i in range(len(s)):
            if s[i] == c:
                prev_left = i
            dist[i] = min(dist[i], i - prev_left)

        prev_right = 10**9
        for i in range(len(s) - 1, -1, -1):
            if s[i] == c:
                prev_right = i
            dist[i] = min(dist[i], prev_right - i)

        return dist
