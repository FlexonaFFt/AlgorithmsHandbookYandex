class Solution:
    def main(self, s: str):
        maximum, current = 0, 1
        for i in range(1, len(s)):
            if s[i] == s[i - 1]:
                current += 1
            if maximum < current:
                maximum = current

        return maximum

if __name__ == '__main__':
    solve = Solution()
    print(solve.main("abcabcbbb"))
