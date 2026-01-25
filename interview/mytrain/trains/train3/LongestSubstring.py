'''
Дано: строка s.
Найти: длину самой длинной подстроки, содержащей не более 2 разных символов.
Зачем на собесе: динамическое окно + hashmap/Counter + правильное сжатие окна.
'''


class Solve:
    def logest_substring(self, string: str):
        left, best, freq = 0, 0, {}

        for right, val in enumerate(string):
            freq[val] = freq.get(val, 0) + 1

            while len(freq) > 2:
                freq[string[left]] -= 1
                if freq[string[left]] == 0:
                    del freq[string[left]]
                left += 1

            best = max(best, right - left + 1)

        return best


if __name__ == '__main__':
    print(Solve().logest_substring("eceba"))
    print(Solve().logest_substring("ccaabbb"))
