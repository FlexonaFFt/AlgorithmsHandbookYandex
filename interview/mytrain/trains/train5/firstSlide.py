'''
Наибольшая подстрока без повторяющихся символов.
Дана строка s. Найти длину самой длинной подстроки
без повторяющихся символов.
'''

from collections import Counter

class Solution:
    def firstSlide(self, string: str) -> int:
        left, best = 0, 0
        freq = Counter()

        for right, value in enumerate(string):
            freq[value] = freq.get(value, 0) + 1

            while freq[value] > 1:
                freq[string[left]] -= 1
                left += 1

            best = max(best, right - left + 1)
        return best


if __name__ == '__main__':
    print(Solution().firstSlide("abcabcbb"))
    print(Solution().firstSlide("bbbbb"))
    print(Solution().firstSlide("pwwkew"))