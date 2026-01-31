class Solution:
    def main(self, nums: list[int], target: int) -> list[int]:
        freq = {}

        for idx, num in enumerate(nums):
            current = target - num
            if current not in freq.keys():
                freq[num] = idx
            else: return [idx, freq[current]]


if __name__ == '__main__':
    print(Solution().main([2,7,11,15], 9))
    print(Solution().main([20,0,0,5,4], 25))