class Solution:
    def main(self, array: list[int], s: int):
        left, window_sum, best = 0, 0, float('inf')
        for right, v in enumerate(array):
            window_sum += v
            while window_sum >= s:
                best = min(best, right - left + 1)
                window_sum -= array[left]
                left += 1

        return 0 if best == float('inf') else best


if __name__ == '__main__':
    print(Solution().main([2,3,1,2,4,3], 7))
