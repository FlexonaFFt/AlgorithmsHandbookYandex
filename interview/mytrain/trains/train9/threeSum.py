class Solution:
    def main(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            left, right = i + 1, n - 1
            while left < right:
                s = nums[i] + nums[left] + nums[right]
                if s < 0: left += 1
                elif s > 0: right -= 1
                else:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

        return output


if __name__ == '__main__':
    print(Solution().main([-1, 0, 1, 2, -1, -4]))