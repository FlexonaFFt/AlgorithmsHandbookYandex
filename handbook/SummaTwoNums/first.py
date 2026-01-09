class Solution:
    def main(self, a, b) -> int:
        return a + b

if __name__ == '__main__':
    n,m = map(int, input().split())
    solve = Solution()
    print(solve.main(n,m))
