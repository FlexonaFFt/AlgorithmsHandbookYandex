'''
Дана строка (возможно, пустая), состоящая из букв A-Z: AAAABBBCCXYZDDDDEEEFFFAAAAAABBBBBBBBBBBBBBBBBBBBBBBBBBBB
Нужно написать функцию RLE, которая на выходе даст строку вида: A4B3C2XYZD4E3F3A6B28
И сгенерирует ошибку, если на вход пришла невалидная строка.
Пояснения: Если символ встречается 1 раз, он остается без изменений; Если символ повторяется более 1 раза, к нему добавляется количество повторений.'''


class MySolve:
    def my_rle_func(self, current_string: str) -> str:
        if not current_string: return ''
        output, start = [], 0

        for i in range(1, len(current_string)):
            if current_string[i] != current_string[i - 1]:
                counter = i - start
                if counter == 1:
                    output.append(current_string[start])
                else: output.append(current_string[start] + str(counter))
                start = i

        counter = len(current_string) - start
        if counter == 1:
            output.append(current_string[start])
        else: output.append(current_string[start] + str(counter))
        return ''.join(output)


if __name__ == '__main__':
    print(MySolve().my_rle_func('AAAABBBBBTTABB'))