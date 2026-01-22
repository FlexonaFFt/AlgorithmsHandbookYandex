class Solution:
    def longest_substring(self, string: str) -> int:
        left, best = 0, 0
        counter = {}

        for right, val in enumerate(string):
            counter[val] = counter.get(val, 0) + 1

            while counter[val] > 1:
                left_char = string[left]
                counter[left_char] -= 1
                if counter[left_char] == 0:
                    del counter[left_char]
                left += 1

            best = max(best, right - left + 1)

        return best


print(Solution().longest_substring("abcabcbb"))
print(Solution().longest_substring("bbbbb"))
print(Solution().longest_substring("abba"))
