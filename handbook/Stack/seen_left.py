import sys
from collections import deque
from typing import List, Tuple

def visibility_left(nums: List[int]) -> List[int]:
    stack: deque[Tuple[int, int]] = deque()
    res = [0] * len(nums)
    for i, a in enumerate(nums):
        seen = 0
        while stack and stack[-1][0] < a:
            _, cnt = stack.pop()
            seen += cnt
        if stack and stack[-1][0] == a:
            val, cnt = stack.pop()
            seen += cnt
            if stack:
                seen += 1
            stack.append((a, cnt + 1))
        else:
            if stack:
                seen += 1
            stack.append((a, 1))
        res[i] = seen
    return res

def main():
    data = sys.stdin.read().strip().split()
    if not data:
        return
    n = int(data[0])
    nums = list(map(int, data[1:1 + n]))
    ans = visibility_left(nums)
    print(" ".join(map(str, ans)))

if __name__ == "__main__":
    main()
