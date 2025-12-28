def main():
    mnoz, answers = set(), []

    n = int(input())
    for _ in range(n):
        m, x = map(int, input().split())

        if m == 1:
            mnoz.add(x)
        if m == 2:
            if x in mnoz:
                answers.append(1)
            else: answers.append(0)

    for ans in answers:
        print(ans)

if __name__ == '__main__':
    main()
