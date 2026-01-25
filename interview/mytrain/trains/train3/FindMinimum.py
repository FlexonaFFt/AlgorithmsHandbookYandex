'''
Дано: массив nums (уникальные элементы), отсортирован по возрастанию и повёрнут.
Найти: минимальный элемент.
Зачем на собесе: бинарный поиск по “сломленной монотонности”.
'''

class Search:
    def searcher(self, nums: list[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else: right = mid

        return nums[left]


if __name__ == '__main__':
    print(Search().searcher(nums=[3,4,5,1,2]))
    print(Search().searcher(nums=[4,5,6,7,0,1,2]))
    print(Search().searcher(nums=[11,13,15,17]))
