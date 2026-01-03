class Solution:
    def main(self, k: int, nums: list[int]) -> int:
        all_mins = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i + k]
            local_minimum = min(window)
            all_mins.append(local_minimum)

        return sum(all_mins)

    def input_function(self):
        n = int(input())
        k = int(input())
        nums = list(map(int, input().split()))

        print(self.main(k=k, nums=nums))


if __name__ == '__main__':
    solve = Solution()
    solve.input_function()
