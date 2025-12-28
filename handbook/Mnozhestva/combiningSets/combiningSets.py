# ML

class Solution:
    def input_func(self):
        spisok = set()
        n = int(input())
        for _ in range(n):
            line = list(map(int, input().split()))

            for element in line[1:]:
                spisok.add(element)
        return spisok

    def main(self):
        print(len(self.input_func()))

if __name__ == '__main__':
    solve = Solution()
    solve.main()
