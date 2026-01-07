class Solution:
    def main(self, string: str, part: str) -> str:
        return "YES" if part in string else "NO"


if __name__ == '__main__':
    solve = Solution()
    string = str(input().strip())
    part = str(input().strip())
    print(solve.main(string, part))
