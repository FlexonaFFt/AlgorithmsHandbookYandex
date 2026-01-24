from collections import Counter

class MySolution:
    def find_substring(self, string: str) -> int:
        left = best = 0

        freq = Counter()
        for right, char in enumerate(string):
            freq[char] = freq.get(char, 0) + 1

            while freq[char] > 1:
                freq[string[left]] -= 1
                if freq[string[left]] == 0:
                    del freq[string[left]]
                left += 1

            best = max(best, right - left + 1)

        return best

class Solution:
    def find_substring(self, s: str) -> int:
        last = {}
        left = best = 0

        for right, ch in enumerate(s):
            if ch in last and last[ch] >= left:
                left = last[ch] + 1
            last[ch] = right
            best = max(best, right - left + 1)

        return best

if __name__ == '__main__':
    print(Solution().find_substring('abcabcbb'))
