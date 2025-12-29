import sys
import math

def main():
    data = sys.stdin.read().strip().split()
    it = iter(data)
    n = int(next(it))
    freq = {}
    for _ in range(n):
        num = int(next(it))
        den = int(next(it))
        g = math.gcd(num, den)
        num_r = num // g
        den_r = den // g
        key = (num_r, den_r)
        freq[key] = freq.get(key, 0) + 1

    best_key = None
    best_cnt = -1

    for (num_r, den_r), cnt in freq.items():
        if cnt > best_cnt:
            best_cnt = cnt
            best_key = (num_r, den_r)
        elif cnt == best_cnt:
            b_num, b_den = best_key
            if num_r * b_den < b_num * den_r:
                best_key = (num_r, den_r)

    print(best_key[0], best_key[1])

if __name__ == "__main__":
    main()
