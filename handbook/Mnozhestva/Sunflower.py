import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)
    try:
        n = int(next(it))
    except StopIteration:
        print("NO")
        return

    freq = {}
    set_offsets = []
    idx = 1
    for _ in range(n):
        k = int(data[idx])
        set_offsets.append((idx, k))
        idx += 1 + k

    for off, k in set_offsets:
        seen = set()
        for j in range(k):
            x = int(data[off + 1 + j])
            if x not in seen:
                seen.add(x)
        for x in seen:
            freq[x] = freq.get(x, 0) + 1

    core_size = 0
    for c in freq.values():
        if c == n:
            core_size += 1
        elif c >= 2:
            print("NO")
            return

    petals = []
    for off, k in set_offsets:
        cnt = 0
        seen = set()
        for j in range(k):
            x = int(data[off + 1 + j])
            if x in seen:
                continue
            seen.add(x)
            if freq.get(x, 0) != n:
                cnt += 1
        petals.append(cnt)

    print("YES")
    print(core_size)
    print(" ".join(map(str, petals)))

if __name__ == "__main__":
    main()
