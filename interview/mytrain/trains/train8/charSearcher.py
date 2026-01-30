from collections import Counter

class YandexBest:
    def main(self, string: str) -> int:
        frequency = Counter(string)

        for idx, char in enumerate(string):
            if frequency[char] == 1: return idx
        return -1


if __name__ == '__main__':
    print(YandexBest().main("leetcode"))
    print(YandexBest().main("eetcode"))
    print(YandexBest().main("eeeecode"))