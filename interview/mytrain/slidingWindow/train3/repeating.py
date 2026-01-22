from collections import Counter

class Solution:
    def repeater(self, string: str, k: int) -> int:
        counter, max_freq = Counter(), 0
        left, best = 0, 0

        for right, val in enumerate(string):
            counter[val] += 1
            max_freq = max(max_freq, counter[val])

            while (right - left + 1) - max_freq > k:
                counter[string[left]] -= 1
                left += 1
            best = max(best, right - left + 1)

        return best


print(Solution().repeater("AABABBA", 1))
