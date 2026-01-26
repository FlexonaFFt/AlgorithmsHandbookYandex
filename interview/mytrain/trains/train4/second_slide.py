'''
Задача: Дана строка s и список слов одинаковой длины.
Найти индексы всех подстрок, которые являются
перестановкой всех слов из списка.
'''

def findSubstring(string: str, words: list[str]):
    if not string or not words:
        return []

    word_len, word_count = len(words[0]), len(words)
    total_length = word_count * word_len
    words_freq, output = {}, []

    for word in words:
        words_freq[word] = words_freq.get(word, 0) + 1

    for right in range(word_len):
        left = right
        counter = 0
        current_freq = {}

        while right + word_len <= len(string):
            word = string[right:right + word_len]
            right += word_len

            if word in words_freq:
                current_freq[word] = current_freq.get(word, 0) + 1
                counter += 1

                while current_freq[word] > words_freq[word]:
                    left_word = string[left:left + word_len]
                    current_freq[left_word] -= 1
                    counter -= 1
                    left += word_len

                if counter == word_count:
                    output.append(left)

            else:
                current_freq.clear()
                counter, left = 0, right

    return output


def run_tests():
    # 1. Простой случай
    # "barfoothefoobarman", слова ["foo","bar"]
    # Ожидаем [0, 9], так как "barfoo" (0) и "foobar" (9) подходят.
    assert sorted(findSubstring("barfoothefoobarman", ["foo","bar"])) == [0, 9]
    print("Test 1 Passed: Простой случай")

    # 2. Слова не могут составить комбинацию (нет нужной последовательности)
    assert findSubstring("wordgoodgoodgoodbestword", ["word","good","best","word"]) == []
    print("Test 2 Passed: Нет соответствий")

    # 3. Пересекающиеся слова и повторы
    # "barfoofoobarthefoobarman", слова ["bar","foo","the"]
    # "foobarthe" начинается с индекса 6, "barthefoo" с индекса 9 и т.д.
    assert sorted(findSubstring("barfoofoobarthefoobarman", ["bar","foo","the"])) == [6, 9, 12]
    print("Test 3 Passed: Пересечения")

    # 4. Все слова одинаковые
    # "aaaaaaaa", слова ["aa","aa"]
    # Индексы 0, 1, 2, 3, 4 (каждые две "aa" подряд)
    assert sorted(findSubstring("aaaaaaaa", ["aa","aa"])) == [0, 1, 2, 3, 4]
    print("Test 4 Passed: Одинаковые слова")

    # 5. Пустая строка или пустой список слов
    assert findSubstring("", ["foo"]) == []
    assert findSubstring("foobar", []) == []
    print("Test 5 Passed: Пустые входные данные")

run_tests()
