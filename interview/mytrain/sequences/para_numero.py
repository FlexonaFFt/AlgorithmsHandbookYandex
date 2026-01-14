def main(nums: list[int], x: int):
    seen = {}
    for i in range(len(nums)):
        dop = x - nums[i]
        if dop in seen:
            return (seen[dop], i)
        seen[nums[i]] = i
    return None

if __name__ == '__main__':
    print(main([2, 7, 11, 15], 9))
