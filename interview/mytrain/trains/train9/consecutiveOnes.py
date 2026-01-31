class Conseq:
    def main(self, nums: list[int], k: int) -> int:
        left, zeros, best = 0, 0, 0

        for right, num in enumerate(nums):
            if num == 0: zeros += 1

            while zeros > k:
                if nums[left] == 0:
                    zeros -= 1
                left += 1
            best = max(best, right - left + 1)
        return best


if __name__ == '__main__':
    print(Conseq().main([1,1,1,0,0,0,1,1,1,1,0], 2))