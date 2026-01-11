def main():
    n = int(input())
    if n <= 6:
        print("No")
        return

    arr = [200000, 1] + list(range(2, n))
    print("Yes")
    print(' '.join(map(str, arr)))

if __name__ == '__main__':
    main()
