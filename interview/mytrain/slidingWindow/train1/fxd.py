class Solve():
    def main(self, nums: list[int], k: int) -> float:
        window = sum(nums[:k])
        best = window

        for r in range(k, len(nums)):
            window += nums[r] - nums[r - k]
            best = max(window, best)

        return best / k


if __name__ == '__main__':
    print(Solve().main([1,12,-5,-6,50,3], 4))
