class Solution:
    def main(self, array: list[int], l: int):
        if l <= 0 or l > len(array):
            return 0

        window_sum = sum(array[:l])
        best = window_sum

        for i in range(l, len(array)):
            window_sum += array[i] - array[i - l]
            if window_sum > best:
                best = window_sum

        return best
