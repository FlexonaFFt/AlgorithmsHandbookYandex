class Solution:
    def main(self, nums: list[int]) -> list[int]:
        n = len(nums)
        output= [1] * n

        left = 1
        for i in range(n):
            output[i] = left
            left *= nums[i]

        right = 1
        for i in range(n - 1, -1, -1):
            output[i] *= right
            right *= nums[i]
        return output


if __name__ == '__main__':
    print(Solution().main([1,2,3,4]))