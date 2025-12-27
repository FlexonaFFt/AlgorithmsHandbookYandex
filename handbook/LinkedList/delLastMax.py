class Solution:
    def function(self, n: int, nums: list[int]):
        max_number, max_position = 0, 0
        for i in range(n):
            if nums[i] > max_number:
                max_number = nums[i]
            if nums[i] == max_number:
                max_position = i
        
        del nums[max_position]
        return nums


if __name__ == '__main__':  
    solution = Solution()
    
    n = int(input())
    nums = list(map(int, input().split()))
    result = solution.function(n, nums)
    print(' '.join(map(str, result)))