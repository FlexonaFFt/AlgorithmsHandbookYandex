'''
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.'''

# Мое решение

class MySolution:
    def finder(self, string: str) -> str:
        if not string: return ''
        posledovatelnost: list[str] = []
        last_symb, counter = string[0], 1

        for symb in string[1:] + '#':
            if symb != last_symb:
                posledovatelnost.append(
                    last_symb if counter == 1 else last_symb + str(counter)
                )
                last_symb, counter = symb, 1

            # Если символ просто повторился
            else: counter += 1
        return ''.join(posledovatelnost)

    # Второй способ решения
    def rle(self, string: str) -> str:
        if not string: return ''
        output, start = [], 0
        for i in range(1, len(string)):
            if string[i] != string[i - 1]:
                counter = i - start
                output.append(string[start] if counter == 1 else string[start] + str(counter))
                start = i

        # Дописываем последний блок
        counter = len(string) - start
        output.append(string[start] if counter == 1 else string[start] + str(counter))
        return ''.join(output)

    # Решение через itertools
    def rle2(self, string: str) -> str:
        from itertools import groupby
        if any(not ("A" <= c <= "z") for c in string):
            raise ValueError("Invalid input")

        return ''.join(
            char if (cnt := len(list(grp))) == 1 else f"{char}{cnt}"
            for char, grp in groupby(string)
        )


# тесты
if __name__ == '__main__':
    solve = MySolution()
    main_test_case = 'AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB'
    print(solve.finder(main_test_case))
    print(solve.rle(main_test_case))
