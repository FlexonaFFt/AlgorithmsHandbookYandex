class Soliton:
    def main(self, nums: list[int], k: int) -> int:
        dict, left, best = {}, 0, 0

        for right, val in enumerate(nums):
            dict[val] = dict.get(val, 0) + 1
            while len(dict) > k:
                dict[nums[left]] -= 1
                if dict[nums[left]] == 0:
                    del dict[nums[left]]
                left += 1

            best = max(best, right - left + 1)

        return best


if __name__ == '__main__':
    print(Soliton().main([1,2,1,2,3], 2))
