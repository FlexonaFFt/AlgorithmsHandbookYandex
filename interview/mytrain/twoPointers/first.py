class Solution:
    def main(self, arr: list[int], s: int):
        left = 0
        right = len(arr) - 1
        output = []

        while left < right:
            current = arr[left] + arr[right]
            if current == s:
                output.append((left, right))
                left += 1
                right -= 1
            elif current < s:
                left += 1
            else: right -= 1
        return output


if __name__ == '__main__':
    solver = Solution()

    # basic example
    a, s = [1, 2, 3, 4, 6, 7], 8
    assert solver.main(a, s) == [(0, 5), (1, 4)]

    # no pairs
    a, s = [1, 2, 3], 10
    assert solver.main(a, s) == []

    # single pair
    a, s = [2, 5, 9, 11], 14
    assert solver.main(a, s) == [(1, 2)]

    # duplicates (unique index pairs in sorted array)
    a, s = [1, 1, 2, 2, 3, 3], 4
    assert solver.main(a, s) == [(0, 5), (1, 4), (2, 3)]

    # negatives
    a, s = [-5, -1, 0, 2, 4, 7], 2
    assert solver.main(a, s) == [(0, 5), (2, 3)]

    print("ok")
