from typing import List

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()
        answer = 0
        i = j = 0 # Два указателя
        while i < len(g) and j < len(s):
            if s[j] >= g[i]:
                answer += 1
                i += 1
                j += 1
            else:
                j += 1
        return answer
