class Solution:
    def main(self, nums: list[int]) -> int:
        sett, best = set(nums), 0
        for x in sett:
            if x - 1 not in sett:
                current, length = x, 1
                while current + 1 in sett:
                    current += 1
                    length += 1
                if length > best:
                    best = length

        return best

    def optimal(self, nums: list[int]) -> int:
        if not nums: return 0
        nums.sort()
        current, maximum = 1, 1

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                continue # пропускаем дубликаты
            if nums[i] == nums[i - 1] + 1:
                current += 1
            else: current = 1
            if current > maximum: maximum = current
        return maximum


solve = Solution()
print(solve.main(nums=[100, 4, 200, 1, 3, 2]))
print(solve.optimal(nums=[100, 4, 200, 1, 3, 2]))
