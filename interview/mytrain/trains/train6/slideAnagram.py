from collections import Counter

class Finder:
    def main(self, s: str, p: str) -> list[int]:
        n, need = len(s), Counter(s)
        window = Counter(p[:n])
        output = []

        if window == need:
            output.append(0)

        for right in range(n, len(p)):
            window[p[right]] += 1
            window[p[right - n]] -= 1
            if window[p[right - n]] == 0: del window[p[right - n]]
            if window == need: output.append(right - n + 1)
        return output


if __name__ == '__main__':
    print(Finder().main('abc', 'cbaebabacd'))