class YandexBestCompany:
    def main(self, string: str) -> bool:
        left, right = 0, len(string) - 1

        while left < right and string[left] == string[right]:
            left += 1
            right -= 1
        if left >= right:
            return True


        i, j = left + 1, right
        ok1 = True

        while i < j:
            if string[i] != string[j]:
                ok1 = False
                break
            i += 1
            j -= 1

        i, j = left, right - 1
        ok2 = True
        while left < j:
            if string[i] != string[j]:
                ok2 = False
                break
            i += 1
            j -= 1

        return ok1 or ok2


    def simpled(self, string: str) -> bool:
        def is_palindrome(left: int, right: int) -> bool:
            while left < right:
                if string[left] != string[right]:
                    return False
                left += 1
                right -= 1
            return True

        left, right = 0, len(string) - 1
        while left < right and string[left] == string[right]:
            left += 1
            right -= 1

        if left >= right:
            return True

        return is_palindrome(left + 1, right) or is_palindrome(left, right - 1)


if __name__ == '__main__':
    print(YandexBestCompany().main('abca'))
    print(YandexBestCompany().main('abc'))

    print(YandexBestCompany().simpled('abca'))
    print(YandexBestCompany().simpled('abc'))