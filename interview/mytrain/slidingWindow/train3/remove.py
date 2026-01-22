class Solution:
    def remover(self, nums: list[int]) -> list[int]:
        seen = set()
        result = []
        for num in nums:
            if num not in seen:
                seen.add(num)
                result.append(num)
        return result

    def etalon(self, nums: list[int]) -> int:
        if not nums: return 0

        slow = 1
        for fast in range(1, len(nums)):
            if nums[fast] != nums[fast - 1]:
                nums[slow] = nums[fast]
                slow += 1
        return slow


print(Solution().remover([1,1,2]))
print(Solution().etalon([1,1,2]))
