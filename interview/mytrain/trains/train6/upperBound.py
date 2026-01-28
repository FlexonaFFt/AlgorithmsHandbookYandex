# В upper_bound - необходимо искать первый элемент, который больше x (> x)

class Bound:
    def upper_bound(self, a: list[int], x: int):
        left, right = 0, len(a)

        while left < right:
            mid = (left + right) // 2
            if a[mid] <= x:
                left = mid + 1
            else:
                right = mid
        return left if left < len(a) else -1


if __name__ == '__main__':
    print(Bound().upper_bound([1, 3, 3, 6, 10], 0))
    print(Bound().upper_bound([1, 3, 3, 6, 10], 3))
    print(Bound().upper_bound([1, 3, 3, 6, 10], 6))
    print(Bound().upper_bound([1, 3, 3, 6, 10], 10))