def main():
    n = int(input().strip())
    arr = list(map(int, input().split()))
    if len(arr) < n:
        while len(arr) < n:
            arr.extend(map(int, input().split()))
        arr = arr[:n]

    # Найдем два максимальных числа одним проходом
    max1 = -1
    max2 = -1
    for x in arr:
        if x > max1:
            max2 = max1
            max1 = x
        elif x > max2:
            max2 = x

    print(max1 * max2)

if __name__ == "__main__":
    main()
