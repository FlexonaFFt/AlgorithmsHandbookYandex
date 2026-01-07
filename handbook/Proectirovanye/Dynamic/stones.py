class Solution:
    def main(self, first: int, second: int) -> str:
        if first % 2 == 0 and second % 2 == 0:
            return "Lose"
        return "Win"


if __name__ == '__main__':
    n, m = map(int, input().split())
    print(Solution().main(n, m))
