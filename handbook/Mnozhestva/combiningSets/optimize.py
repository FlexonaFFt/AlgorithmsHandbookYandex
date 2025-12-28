import sys

MAX_X = 1_000_000
BITSET_SIZE = (MAX_X // 8) + 1
bitset = bytearray(BITSET_SIZE)

POPCOUNT = bytes(bin(i).count("1") for i in range(256))

def ints():
    buf_read = sys.stdin.buffer.readline
    while True:
        line = buf_read()
        if not line:
            return
        for tok in line.split():
            yield int(tok)

def set_bit(v: int) -> None:
    bitset[v >> 3] |= 1 << (v & 7)

def main():
    it = ints()

    try:
        n = next(it)
    except StopIteration:
        print(0)
        return

    for _ in range(n):
        k = next(it)
        for _ in range(k):
            x = next(it)
            if 1 <= x <= MAX_X:
                set_bit(x)

    total = 0
    for b in bitset:
        total += POPCOUNT[b]
    print(total)

if __name__ == "__main__":
    main()
