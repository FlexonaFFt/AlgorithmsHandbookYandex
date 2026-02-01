from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()

        for right, value in enumerate(nums):
            if right > k:
                window.remove(nums[right - k - 1])

            if value in window:
                return True

            window.add(value)

        return False

# Runtime 34 ms
if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate([1,2,3,1], 3))
    print(Solution().containsNearbyDuplicate([1,0,1,1], 1))
    print(Solution().containsNearbyDuplicate([1,2,3,1,2,3], 2))