'''Условие: s1, s2. Проверить, есть ли в s2 подстрока — перестановка s1.'''

from collections import Counter

class Solution:
    def finder(self, s1: str, s2: str) -> bool:
        need, n= Counter(s1), len(s1)
        window = Counter(s2[:n])
        if n > len(s2): return False
        if window == need: return True

        for i in range(n, len(s2)):
            window[s2[i]] += 1
            left_char = s2[i - n]
            window[left_char] -= 1
            if window[left_char] == 0:
                del window[left_char]
            if window == need:
                return True
        return False


if __name__ == '__main__':
    print(Solution().finder('ab', 'eidbaooo'))
    print(Solution().finder('ab', 'eidaooo'))