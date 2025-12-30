from collections import deque
import sys

def main():
    data = sys.stdin.buffer.read().split()
    it = iter(data)

    try:
        q = int(next(it))
    except StopIteration:
        print()  
        return

    d = deque()
    out = []

    for _ in range(q):
        t = int(next(it))
        if t == 1:
            x = int(next(it))
            d.appendleft(x)
        elif t == 2:
            x = int(next(it))
            d.append(x)
        elif t == 3:
            if d:
                d.popleft()
        else:  
            if d:
                d.pop()

        if d:
            out.append(f"{d[0]} {d[-1]}")
        else:
            out.append("-1")

    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()