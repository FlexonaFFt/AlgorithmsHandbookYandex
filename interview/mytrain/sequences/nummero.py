def main(nums: list[int]) -> int:
    counter_list = {}
    for numero in nums:
        counter_list[numero] = counter_list.get(numero, 0) + 1
    for idx, numero in enumerate(nums):
        if counter_list[numero] == 2: return idx
    return -1


if __name__ == '__main__':
    print(main([4, 5, 1, 2, 0, 2, 1, 4, 5]))
