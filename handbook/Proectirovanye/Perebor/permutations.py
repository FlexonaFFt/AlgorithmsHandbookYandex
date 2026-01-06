class Tools:
    @staticmethod
    def factorial(n: int) -> int:
        p = 1
        for i in range(1, n + 1):
            p *= i
        return p

    def permutations(self, n: int) -> int:
        return self.factorial(n)

    def combinations(self, n: int, k: int) -> int:
        fact = self.factorial(n)
        denominator = self.factorial(k) * self.factorial(n - k)
        return fact // denominator

    def combinations_with_rep(self, n: int, k: int) -> int:
        nominator = self.factorial(n + k - 1)
        denominator = self.factorial(k) * self.factorial(n - 1)
        return nominator // denominator

if __name__ == '__main__':
    n, k = map(int, input().split())
    solve = Tools()
    print(solve.combinations_with_rep(n, k))
