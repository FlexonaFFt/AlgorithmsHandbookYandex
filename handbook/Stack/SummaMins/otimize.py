class Solution:
    def main(self, k: int, nums: list[int]) -> int:
        from collections import deque 
        all_mins, total = deque(), 0

        for i in range(len(nums)):
            while all_mins and nums[all_mins[-1]] >= nums[i]:
                all_mins.pop()
            all_mins.append(i)

            window_start = i - k + 1
            while all_mins and all_mins[0] < window_start:
                all_mins.popleft()

            if i >= k - 1:
                total += nums[all_mins[0]]
        return total

    def input_function(self):
        n = int(input())
        k = int(input())
        nums = list(map(int, input().split()))

        print(self.main(k=k, nums=nums))


if __name__ == '__main__':
    solve = Solution()
    solve.input_function()
