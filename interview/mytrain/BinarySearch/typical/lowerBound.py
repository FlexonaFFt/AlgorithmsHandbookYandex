'''дан отсортированный массив a и число x. Найди первый индекс, где a[i] >= x.
Если все элементы меньше x, верни len(a).'''

class Solution:
    def lower_bound(self, array: list[int], x: int) -> int:
        left, right = 0, len(array)  # right = len(array), а не len(array)-1
        while left < right:
            mid = (left + right) // 2
            if array[mid] >= x:
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == '__main__':
    print(Solution().lower_bound([7,8,9,10,11,12], 13))  # 6
    print(Solution().lower_bound([7,8,9,10,11,12], 10))  # 3
    print(Solution().lower_bound([7,8,9,10,11,12], 6))   # 0
