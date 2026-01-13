class Solution:
    def main(self, s: str) -> int:
        left, max_len, seen = 0, 0, set()
        for right, char in enumerate(s):
            while char in seen:
                seen.remove(s[left])
                left += 1
            seen.add(char)
            max_len = max(max_len, right - left + 1)
        return max_len



if __name__ == '__main__':
    solve = Solution()
    print(solve.main("abcaabcdba"))
    print(solve.main("abba"))
    print(solve.main("tmmzuxt"))
