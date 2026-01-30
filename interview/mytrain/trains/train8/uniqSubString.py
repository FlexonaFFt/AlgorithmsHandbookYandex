from collections import Counter

class Yandex:
    # Мой код содержит логические ошибки, поэтому он не работает
    def uniquer(self, string: str, pattern: str) -> str:
        left, output, curr = 0, string, Counter()

        for right, char in enumerate(string):
            if char in pattern:
                curr[char] = curr.get(char, 0) + 1

            while curr[char] > 1:
                curr[string[left]] -= 1
                if curr[string[left]] == 0:
                    del curr[string[left]]
                left += 1

            if len(output) > len(string[left:right]):
                output = string[left:right]

        return output if len(output) != len(string) else ''

    # Вот корректная версия кода, которая правильно работает и у которой не нарушена основная логика
    def corrected(self, string: str, pattern: str) -> str:
        if not string or not pattern:
            return ''

        need, curr = Counter(pattern), Counter()
        required, formed = len(need), 0
        left, best, output = 0, float('inf'), ''

        for right, char in enumerate(string):
            if char in need:
                curr[char] = curr.get(char, 0) + 1
                if curr[char] == need[char]:
                    formed += 1

            while formed == required:
                current_window = right - left + 1
                if current_window < best:
                    best = current_window
                    output = string[left:right + 1]

                left_char = string[left]
                if left_char in need:
                    curr[left_char] -= 1
                    if curr[left_char] < need[left_char]:
                        formed -= 1

                left += 1
        return output


if __name__ == '__main__':
    print(Yandex().corrected("ADOBECODEBANC", "ABC"))