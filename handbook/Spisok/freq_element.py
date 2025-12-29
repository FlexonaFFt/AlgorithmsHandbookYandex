class Solution:
    def main(self, nums: list[int]):
        spisok = {}
        for num in nums:
            if num not in spisok:
                spisok[num] = 1
            else:
                spisok[num] += 1

        best_num, best_cnt = None, -1
        for num, cnt in spisok.items():
            if cnt > best_cnt or (
                cnt == best_cnt and (
                    best_num is None or num < best_num
                )
            ):
                best_num = num
                best_cnt = cnt
        return best_num

if __name__ == '__main__':
    solve = Solution()
    n = int(input())
    nums = list(map(int, input().split()))
    print(solve.main(nums))
