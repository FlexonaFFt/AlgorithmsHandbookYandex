from collections import Counter

class Simple:
    def slide(self, string: str) -> int:
        left, best, curr = 0, 0, Counter()

        for right, char in enumerate(string):
            curr[char] = curr.get(char, 0) + 1

            while curr[char] > 1:
                left_char = string[left]
                curr[left_char] -= 1
                if curr[left_char] == 0:
                    del curr[left_char]
                left += 1

            best = max(best, right - left + 1)

        return best


if __name__ == '__main__':
    print(Simple().slide("abcabcbb"))