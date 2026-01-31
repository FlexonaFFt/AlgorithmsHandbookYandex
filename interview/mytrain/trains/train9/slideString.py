from collections import Counter

class Solution:
    def mainSlider(self, string: str, idx: int):
        left, best, out, freq = 0, 0, '', Counter()

        for right, char in enumerate(string):
            freq[char] = freq.get(char, 0) + 1

            while len(freq) > idx:
                curr_left_ch = string[left]
                freq[curr_left_ch] -= 1
                if freq[curr_left_ch] == 0:
                    del freq[curr_left_ch]
                left += 1

            current_length = right - left + 1
            if best < (current_length):
                best = current_length
                out = string[left: right+1]

        return [best, out]


def test_func():
    current_solve = Solution()
    print(current_solve.mainSlider('eceba', 2))
    print(current_solve.mainSlider('ecaba', 2))
    print(current_solve.mainSlider('eccba', 3))


if __name__ == '__main__':
    test_func()