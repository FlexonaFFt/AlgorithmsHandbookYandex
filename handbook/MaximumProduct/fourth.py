class Solution:
    def main(self, array: list[int]):
        max1 = max2 = max3 = max4 = -10**8
        min1 = min2 = min3 = min4 = 10**8

        for x in array:
            if x > max1:
                max4 = max3
                max3 = max2
                max2 = max1
                max1 = x
            elif x > max2:
                max4 = max3
                max3 = max2
                max2 = x
            elif x > max3:
                max4 = max3
                max3 = x
            elif x > max4:
                max4 = x

            if x < min1:
                min4 = min3
                min3 = min2
                min2 = min1
                min1 = x
            elif x < min2:
                min4 = min3
                min3 = min2
                min2 = x
            elif x < min3:
                min4 = min3
                min3 = x
            elif x < min4:
                min4 = x

        p1 = max1 * max2 * max3 * max4
        p2 = max1 * max2 * min1 * min2
        p3 = min1 * min2 * min3 * min4
        answer = max(p1, p2, p3)
        print(answer)


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    solve = Solution()
    solve.main(nums)
