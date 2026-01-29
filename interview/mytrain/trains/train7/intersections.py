#Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
#Надо вернуть [1, 2, 2, 3] (порядок неважен)

from collections import Counter

class Solution:
    def main(self, nums1: list[int], nums2: list[int]) -> list[int]:
        set_dict, result = Counter(nums2), []
        for num in nums1:
            count = set_dict[num]
            if count > 0:
                result.append(num)
                set_dict[num] -= 1

        return result


if __name__ == '__main__':
    print(Solution().main([1, 2, 3, 2, 0], [5, 1, 2, 7, 3, 2]))
