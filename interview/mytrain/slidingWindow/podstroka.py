class Solution:
    def main(self, string: str) -> int:
        max_result = left = 0
        window = set()
        for right, ch in enumerate(string):
            while ch in window:
                window.remove(string[left])
                left += 1

            window.add(ch)
            max_result = max(max_result, right - left + 1)

        return max_result


if __name__ == '__main__':
    print(Solution().main(string='abcabcbb'))
