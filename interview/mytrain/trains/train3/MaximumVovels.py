'''
Задача: Maximum Number of Vowels in a Substring of Given Length

Дано: строка s и число k.
Найти: максимальное количество гласных (a,e,i,o,u) среди всех подстрок длины k.
Зачем на собесе: фиксированное окно + аккуратная поддержка счётчика.
'''

class Solution:
    def maximum_vovels(self, string: str, k: int) -> int:
        all_vovels = 'aeiou'
        current = sum(1 for ch in string[:k] if ch in all_vovels)
        best = current

        for right in range(k, len(string)):
            left = right - k
            if string[left] in all_vovels:
                current -= 1
            if string[right] in all_vovels:
                current += 1
            best = max(best, current)

        return best


if __name__ == '__main__':
    print(Solution().maximum_vovels("abciiidef", 3))
    print(Solution().maximum_vovels("leetcode", 2))
