from typing import List

class MySolve:
    def seqFinder(self, nums: List[int], s: int) -> int:
        left, current_summa, minimal = 0, 0, float('inf')

        for right, value in enumerate(nums):
            current_summa += nums[right]
            while current_summa >= s:
                minimal = min(minimal, right - left + 1)
                current_summa -= nums[left]
                left += 1

        if minimal == float('inf'): return 0
        else: return minimal


if __name__ == '__main__':
    print(MySolve().seqFinder([2, 3, 1, 2, 4, 3], 12))