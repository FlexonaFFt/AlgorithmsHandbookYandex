def main():
    n, m = map(int, input().split())
    A, B = [], []

    for _ in range(n):
        row = list(map(int, input().split()))
        A.append(row)

    for _ in range(n):
        row = list(map(int, input().split()))
        B.append(row)

    for i in range(n):
        row = []
        for j in range(m):
            line = str(A[i][j] + B[i][j])
            row.append(line)
        print(" ".join(row))


if __name__ == '__main__': main()
