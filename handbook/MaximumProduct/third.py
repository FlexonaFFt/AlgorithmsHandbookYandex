class Solution:
    def main(self, array: list[int]):
        max1 = max2 = max3 = -10**8
        min1 = min2 = 10**8

        for x in array:
            if x > max1:
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max3 = max2
                max2 = x
            elif x > max3:
                max3 = x

            if x < min1:
                min2 = min1
                min1 = x
            elif x < min2:
                min2 = x

        p1 = max1 * max2 * max3
        p2 = max1 * min1 * min2
        answer = p1 if p1 >= p2 else p2
        print(answer)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    solve = Solution()
    solve.main(nums)
