'''
Search in Rotated Sorted Array II -- LeetCode
'''


class Solution:
    def search(self, nums: list[int], target: int) -> bool:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            if nums[left] == nums[mid]:
                left += 1
                continue

            if nums[left] < nums[mid]:
                if nums[left] <= target <= nums[mid]:
                    right = mid - 1
                else: left = mid + 1

            else:
                if nums[mid] < target <= nums[right]:
                    left = mid + 1
                else: right = mid - 1

        return False


if __name__ == '__main__':
    print(Solution().search([2,5,6,0,0,1,2], 0))
    print(Solution().search([2,5,6,0,0,1,2], 3))
