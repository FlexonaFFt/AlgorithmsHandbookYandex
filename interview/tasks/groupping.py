'''
Sample Input ["eat", "tea", "tan", "ate", "nat", "bat"]
Sample Output [ ["ate", "eat", "tea"], ["nat", "tan"], ["bat"] ]

Т.е. сгруппировать слова по "общим буквам".
'''

# Решение с хабра
from collections import defaultdict, Counter

class Habr:
    def main(self, in_string: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for word in in_string:
            key = tuple(sorted(word))
            groups[key].append(word)

        return [sorted(in_string) for in_string in groups.values()]


class Solutions:
    # Решение через частотный ключ O(n * k)
    def group_by_count(self, words: list[str]) -> list[list[str]]:
        groups = defaultdict(list)

        for w in words:
            freq = [0] * 26
            for char in w:
                freq[ord(char) - ord('a')] += 1
            groups[tuple(freq)].append(w)

        return [sorted(v) for v in groups.values()]

    # Решение, где клюс как счетчик символов
    def group_by_counter(self, words: list[str]) -> list[list[str]]:
        groups = defaultdict(list)
        for w in words:
            groups[tuple(sorted(Counter(w).items()))].append(w)
        return [sorted(v) for v in groups.values()]


if __name__ == '__main__':
    habr, test = Habr(), ["eat", "tea", "tan", "ate", "nat", "bat"]
    solve = Solutions()
    print(habr.main(in_string=test))

    print(solve.group_by_count(test))
    print(solve.group_by_counter(test))
