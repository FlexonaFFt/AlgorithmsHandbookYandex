class Solution:
    def main(self, array: list[int], k: int) -> int:
        left = 0
        maxlen = 0
        max_q: list[int] = []
        min_q: list[int] = []

        for right, value in enumerate(array):
            while max_q and array[max_q[-1]] < value:
                max_q.pop()
            max_q.append(right)

            while min_q and array[min_q[-1]] > value:
                min_q.pop()
            min_q.append(right)

            while array[max_q[0]] - array[min_q[0]] > k:
                if max_q[0] == left:
                    max_q.pop(0)
                if min_q[0] == left:
                    min_q.pop(0)
                left += 1

            maxlen = max(maxlen, right - left + 1)

        return maxlen


if __name__ == '__main__':
    a, k = [8, 2, 4, 7], 4
    print(Solution().main(a, k))
