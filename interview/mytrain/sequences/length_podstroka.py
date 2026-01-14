def self(array: list[int], k: int) -> int:
    l, current, best = 0, 0, 0
    for r in range(len(array)):
        current += array[r]
        while current > k and l <= r:
            current -= array[l]
            l += 1
        best = max(best, r - l + 1)
    return best

print(self([2, 1, 3, 2, 4, 1], 7))
