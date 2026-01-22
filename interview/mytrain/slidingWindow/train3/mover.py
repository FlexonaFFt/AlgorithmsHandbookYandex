class Solution:
    # O(n ** 2)
    def mymover(self, nums: list[int]):
        zeros = 0

        for num in nums:
            if num == 0:
                zeros += 1

        for _ in range(zeros):
            nums.remove(0)
            nums.append(0)
        return nums

    # O(n)
    def optimize(self, nums: list[int]):
        slow = 0

        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1

        for i in range(slow, len(nums)):
            nums[i] = 0
        return nums


print(Solution().mymover([0,1,0,3,12]))
print(Solution().optimize([0,1,0,3,12]))
