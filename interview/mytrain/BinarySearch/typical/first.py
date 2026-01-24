'''дан отсортированный список a (по возрастанию) и число x.
Верни индекс x, иначе -1.'''

class Solution:
    def main(self, array: list[int], x: int) -> int:
        left, right = 0, len(array) - 1
        while left <= right:
           mid = (left + right) // 2 # находим середину array
           if array[mid] == x: return mid
           elif array[mid] < x: left = mid + 1
           else: right = mid - 1
        return -1


if __name__ == '__main__':
    print(Solution().main([0,0,4,5,6], 6))
    print(Solution().main([0,0,4,5,6], 0))
    print(Solution().main([0,0,4,5,6], 5))
