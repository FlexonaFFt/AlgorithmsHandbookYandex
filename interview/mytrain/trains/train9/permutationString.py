from collections import Counter

class Solution:
    def permutatorFinder(self, s1: str, s2: str) -> bool:
        left, pattern, perm = 0, Counter(s1), Counter()

        for right, char in enumerate(s2):
            perm[char] = perm.get(char, 0) + 1

            while right - left + 1 > len(s1):
                left_char = s2[left]
                perm[left_char] -= 1
                if perm[left_char] == 0:
                    del perm[left_char]
                left += 1

            if right - left + 1 == len(s1):
                if perm == pattern:
                    return True
        return False


if __name__ == '__main__':
    print(Solution().permutatorFinder('ab', 'eidbaooo'))