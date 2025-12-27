class Solution:
    def counter(self, nums: list[int]):
        current_min, result = 10 * 10**8, []
        for x in nums:
            if x < current_min:
                current_min = x
            result.append(current_min)

        print(' '.join(map(str, result)))

if __name__ == '__main__':
    solve = Solution()

    n = int(input())
    numbers = list(map(int, input().split()))
    solve.counter(numbers)