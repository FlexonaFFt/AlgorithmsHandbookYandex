from collections import deque

class Solution:
    def main(self):
        d, out = deque(), []
        n = int(input())
        for _ in range(n):
            line = list(map(int, input().split()))
            if line[0] == 1:
                d.append(line[1])
                out.append(str(d[-1]))
            else:
                d.pop()
                out.append(str(d[-1] if d else -1))

        print('\n'.join(out))

if __name__ == '__main__':
    solve = Solution()
    solve.main()
