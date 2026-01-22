class Solution():
    def longest_substring(self, string: str) -> int:
        left, best, counter = 0, 0, {}

        for right, val in enumerate(string):
            counter[val] = counter.get(val, 0) + 1

            while counter[val] > 1:
                counter[string[left]] -= 1
                left += 1

                if counter[string[left]] == 0:
                    del counter[string[left]]

            best = max(best, right - left + 1)

        return best


print(Solution().longest_substring("abcabcbb"))
print(Solution().longest_substring("bbbbb"))
print(Solution().longest_substring("abba"))
