class Solution:
    def max_window(self, s: str) -> int:
        left, best = 0, 0

        for right in range(len(s)):
            if s[right] != s[left]:
                left = right
            best = max(best, right - left + 1)
        return best


if __name__ == '__main__':
    print(Solution().max_window("aaabbbaa"))
