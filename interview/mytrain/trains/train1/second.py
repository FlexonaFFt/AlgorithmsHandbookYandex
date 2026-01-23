from collections import Counter

class Solution:
    def main(self, string: str) -> int:
        left, best, current = 0, 0, Counter()

        for right, val in enumerate(string):
            current[val] = current.get(val, 0) + 1

            while current[val] > 1:
                current[string[left]] -= 1
                if current[string[left]] == 0:
                    del current[string[left]]
                left += 1

            best = max(best, right - left + 1)

        return best


print(Solution().main("abcabcbb"))
