def find_dup(nums: list[int]) -> list[int]:
    out = []
    for i in nums:
        if i not in out:
            out.append(i)
    return out


if __name__ == '__main__':
    print(find_dup([1, 2, 2, 3, 1, 4]))
    print(find_dup([5,5,5]))