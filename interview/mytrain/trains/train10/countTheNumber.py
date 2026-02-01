from typing import List
from collections import Counter

class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        left, pairs, output = 0, 0, 0
        counter, n = Counter(), len(nums)

        for right, value in enumerate(nums):
            pairs += counter[value]
            counter[value] += 1

            while pairs >= k:
                output += n - right
                counter[nums[left]] -= 1
                if counter[nums[left]] == 0:
                    del counter[nums[left]]

                pairs -= counter[nums[left]]
                left += 1

        return output


if __name__ == '__main__':
    print(Solution().countGood([1,1,1,1,1], 10))
    print(Solution().countGood([3,1,4,3,2,2,4], 2))