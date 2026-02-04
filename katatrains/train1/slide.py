from collections import Counter
from typing import List

class Window:
    def slider(self, nums: List[int], k: int) -> int:
        if k <= 0 or k > len(nums): return 0
        curr = sum(nums[:k])
        best = curr

        for i in range(k, len(nums)):
            curr += nums[i] - nums[i - k]
            if curr > best: best = curr
        return best


if __name__ == '__main__':
    print(Window().slider([2, 1, 5, 1, 3, 2], 3))
    print(Window().slider([-1, -3, -2], 2))