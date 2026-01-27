'''
Задача: Разделить массив (Split Array Largest Sum).
Дан массив nums и число k. Нужно разделить массив на k
непрерывных подмассивов так, чтобы максимальная сумма
среди этих подмассивов была минимально возможной.
'''


class MyConversion:
    def canSplit(self, max_sum: int, nums: list[int], target: int) -> bool:
        current_sum, counter = 0, 1
        for num in nums:
            if current_sum + num <= max_sum:
                current_sum += num
            else:
                counter += 1
                current_sum = num
        return counter <= target

    def myBinarySearcher(self, nums: list[int], target: int) -> int:
        low, high = max(nums), sum(nums)
        output = high

        while low <= high:
            mid = (low + high) // 2
            if self.canSplit(mid, nums, target):
                output = mid
                high = mid - 1

            else: low = mid + 1

        return output


if __name__ == '__main__':
    print(MyConversion().myBinarySearcher([5, 4, 3, 2, 1], 3))
    print(MyConversion().myBinarySearcher([7, 2, 5, 10, 8], 2))