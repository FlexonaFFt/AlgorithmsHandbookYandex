class Solution:
    def main(self, n, first, m, second):
        a = list(first)
        b = list(second)
        k = max(n, m)

        if len(a) < k + 1:
            a = [0] * (k + 1 - len(a)) + a
        if len(b) < k + 1:
            b = [0] * (k + 1 - len(b)) + b

        c = [ai + bi for ai, bi in zip(a, b)]
        print(k)
        print(" ".join(str(x) for x in c))

if __name__ == '__main__':
    n = int(input().strip())
    first = map(int, input().split())
    m = int(input().strip())
    second = map(int, input().split())
    solve = Solution()
    solve.main(n, first, m, second)
