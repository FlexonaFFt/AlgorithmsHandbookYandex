from collections import Counter

class Solution:
    def counter(self, fruits: list[int]) -> int:
        left, maximum, current = 0, 0, Counter()

        for right, fruit in enumerate(fruits):
            current[fruit] = current.get(fruit, 0) + 1

            while len(current) > 2:
                current[fruits[left]] -= 1
                if current[fruits[left]] == 0:
                    del current[fruits[left]]
                left += 1

            maximum = max(maximum, right - left + 1)
        return maximum


if __name__ == '__main__':
    print(Solution().counter([1,2,1]))
    print(Solution().counter([3,3,3,1,2,1,1,2,3,3,4]))