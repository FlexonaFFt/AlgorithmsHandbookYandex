class Solution:
    def main(self, nums: list[int], target: int) -> list[list[int]]:
        left, result, prod = 0, [], 1

        for right, val in enumerate(nums):
            prod *= nums[right]

            while prod >= target:
                prod = prod / nums[left]
                left += 1

            for start in range(left, right + 1):
                result.append(nums[start:right+1])

        return result


if __name__ == '__main__':
    print(Solution().main([10, 5, 2, 6], 100))
