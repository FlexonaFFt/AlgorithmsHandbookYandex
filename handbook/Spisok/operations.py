def operator():
    import sys

    n = int(sys.stdin.readline())
    store = {}
    out = []

    for _ in range(n):
        parts = sys.stdin.readline().split()
        t = int(parts[0])
        if t == 1:
            x = int(parts[1])
            y = int(parts[2])
            store[x] = y
        else:
            x = int(parts[1])
            out.append(str(store.get(x, -1)))

    print("\n".join(out))


if __name__ == '__main__':
    operator()
