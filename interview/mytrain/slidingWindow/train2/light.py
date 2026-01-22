class Solution:
    def main(self, nums: list[int], k: int, threshold: int):
        window = sum(nums[:k])
        counter = 0

        if window >= k * threshold: counter += 1

        for r in range(k, len(nums)):
            window += nums[r] - nums[r - k]
            if window >= k * threshold:
                counter += 1

        return counter


if __name__ == '__main__':
    print(Solution().main([2,2,2,2,5,5,5,8], 3, 4))
