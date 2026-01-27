'''
Тройная сумма (3Sum). Дано целое число nums.
Найдите все уникальные тройки, сумма которых равна нулю.
'''

class Solution:
    def main(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        output: list[list[int]] = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            if nums[i] > 0:
                break

            left, right = i + 1, len(nums) - 1
            while left < right:
                summa = nums[i] + nums[left] + nums[right]
                if summa == 0:
                    output.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:
                        left += 1
                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif summa < 0: left += 1
                else: right -= 1

        return output


if __name__ == '__main__':
    print(Solution().main([-1, 0, 1, 2, -1, -4]))
    print(Solution().main([0, 0, 0]))