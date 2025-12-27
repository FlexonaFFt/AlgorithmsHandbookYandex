class Solution:
    def finder(self, n: int, nums: list[int]):
        is_local_min = [False] * n
        for i in range(1, n - 1):
            if nums[i - 1] > nums[i] < nums[i + 1]:
                is_local_min[i] = True

        remaining = [nums[i] for i in range(n) if not is_local_min[i]]
        print(len(remaining))
        if remaining: print(' '.join(map(str, remaining)))
        else: print()


if __name__ == '__main__':
    solve = Solution()

    n = int(input())
    numbers = list(map(int, input().split()))
    solve.finder(n, numbers)