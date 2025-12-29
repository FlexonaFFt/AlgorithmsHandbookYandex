def main():
    n = int(input())
    data = list(map(int, input().split()))

    frequence = {}
    for num in data:
        frequence[num] = frequence.get(num, 0) + 1

    items = [(val, cnt) for val, cnt in frequence.items()]
    items.sort(key=lambda t: (-t[1], t[0]))
    top3 = [items[0][0], items[1][0], items[2][0]]
    top3.sort()
    print(*top3)

if __name__ == '__main__':
    main()
