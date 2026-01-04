#Даны два массива: [1, 2, 3, 2, 0] и [5, 1, 2, 7, 3, 2]
#Надо вернуть [1, 2, 2, 3] (порядок неважен)

# Решение без множеств
from collections import defaultdict

def common_elements(nums1: list[int], nums2: list[int]) -> list[int]:
    set_dict = defaultdict(int)
    for num in nums2:
        set_dict[num] += 1

    result = []
    for num in nums1:
        count = set_dict[num]
        if count > 0:
            result.append(num)
            set_dict[num] -= 1

    return result

# Решение через множества
def find_common(nums1: list[int], nums2: list[int]) -> list[int]:
    common = set(nums1).intersection(set(nums2))
    for element in common:
        occurs = min(nums1.count(element), nums2.count(element))
