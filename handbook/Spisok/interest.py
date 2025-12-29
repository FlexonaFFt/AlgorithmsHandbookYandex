import sys
from collections import defaultdict

def main():
    data = sys.stdin.read().splitlines()
    if not data:
        print(0)
        return
    try:
        n = int(data[0].strip())
    except:
        print(0)
        return
    words = [line.rstrip("\n") for line in data[1:1+n]]
    if n <= 1:
        print(0)
        return
    L = len(words[0])
    for w in words:
        if len(w) != L:
            print(0)
            return

    word_freq = defaultdict(int)
    for w in words:
        word_freq[w] += 1
    same_pairs = 0
    for f in word_freq.values():
        if f >= 2:
            same_pairs += f * (f - 1) // 2

    total = 0
    for i in range(L):
        mask_cnt = defaultdict(int)
        for w in words:
            m = w[:i] + '#' + w[i+1:]
            mask_cnt[m] += 1
        for c in mask_cnt.values():
            if c >= 2:
                total += c * (c - 1) // 2

    ans = total - L * same_pairs
    print(ans)

if __name__ == "__main__":
    main()
