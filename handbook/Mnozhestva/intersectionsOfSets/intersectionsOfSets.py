import sys

class Solution:
    def input_func(self):
        freq = {}
        data = sys.stdin.read().strip().split()
        it = iter(data)
        try: n = int(next(it))
        except StopIteration:
            print(0)
            return

        for _ in range(n):
            k = int(next(it))
            current_set = set()
            for _ in range(k):
                x = int(next(it))
                current_set.add(x)
            for x in current_set:
                freq[x] = freq.get(x, 0) + 1

        cnt_intersection = 0
        for x_count in freq.values():
            if x_count == n: cnt_intersection += 1
        print(cnt_intersection)

    def main(self):
        self.input_func()

if __name__ == '__main__':
    solve = Solution()
    solve.main()
