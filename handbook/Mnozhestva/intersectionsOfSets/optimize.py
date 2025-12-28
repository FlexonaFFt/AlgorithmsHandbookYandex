import sys

def read_ints_line():
    line = sys.stdin.readline()
    if not line:
        return None
    return list(map(int, line.strip().split()))

def main():
    first = sys.stdin.readline()
    if not first:
        print(0)
        return
    n = int(first.strip())

    offsets = []
    for _ in range(n):
        pos = sys.stdin.tell()
        line = sys.stdin.readline()
        if not line:
            print(0)
            return
        parts = line.strip().split()
        if not parts:
            offsets.append((pos, 0))
            continue
        k = int(parts[0])
        offsets.append((pos, k))

    min_idx = min(range(n), key=lambda i: offsets[i][1])
    sys.stdin.seek(offsets[min_idx][0])
    parts = sys.stdin.readline().strip().split()
    k0 = int(parts[0])
    intersection = set(map(int, parts[1:1 + k0]))

    for i in range(n):
        if i == min_idx:
            continue
        sys.stdin.seek(offsets[i][0])
        parts = sys.stdin.readline().strip().split()
        ki = int(parts[0])

        current = set(map(int, parts[1:1 + ki]))
        intersection.intersection_update(current)
        if not intersection:
            print(0)
            return

    print(len(intersection))


if __name__ == '__main__':
    main()
