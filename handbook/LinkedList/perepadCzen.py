class Solution:
    def finder(self, n: int,  nums: list[int]):
        min_left_val, min_left_idx = nums[0], 0
        max_left_val, max_left_idx = nums[0], 0
        best_min = (nums[0] - nums[1], 0, 1) if n >= 2 else (0, 0, 0)
        best_max = (nums[0] - nums[1], 0, 1) if n >= 2 else (0, 0, 0)

        for j in range(1, n):
            cand_min_val = min_left_val - nums[j]
            cand_min = (cand_min_val, min_left_idx, j)
            if (cand_min[0] < best_min[0] or
            (cand_min[0] == best_min[0] and (cand_min[1] < best_min[1] or
                                             (cand_min[1] == best_min[1] and cand_min[2] < best_min[2])))):
                                             best_min = cand_min

            cand_max_val = max_left_val - nums[j]
            cand_max = (cand_max_val, max_left_idx, j)
            if (cand_max[0] > best_max[0] or
            (cand_max[0] == best_max[0] and (cand_max[1] < best_max[1] or
                                             (cand_max[1] == best_max[1] and cand_max[2] < best_max[2])))):
                                            best_max = cand_max
            
            if nums[j] < min_left_val:
                min_left_val = nums[j]
                min_left_idx = j
            if nums[j] > max_left_val:
                max_left_val = nums[j]
                max_left_idx = j
            
        i1, j1 = best_min[1] + 1, best_min[2] + 1
        i2, j2 = best_max[1] + 1, best_max[2] + 1

        print(i1, j1)
        print(i2, j2)

def input_for_solution():
    n = int(input().strip())
    lst = list(map(int, input().split()))

    solve = Solution()
    solve.finder(n=n, nums=lst)

if __name__ == '__main__':
    input_for_solution()