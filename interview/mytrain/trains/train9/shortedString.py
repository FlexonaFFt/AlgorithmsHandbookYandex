'''
'AAAABBBCCCCCTTDDKMB' -> '4A3B5C2T2DKMB'
'''

class Solution:
    def main(self, string: str) -> str:
        if not string: return ''

        output, counter = [], 1
        for i in range(1, len(string)):
            if string[i] == string[i - 1]:
                counter += 1
            else:
                if counter > 1:
                    output.append(f"{counter}{string[i - 1]}")
                else: output.append(string[i - 1])
                counter = 1

        if counter > 1:
            output.append(f"{counter}{string[i - 1]}")
        else: output.append(string[-1])
        return ''.join(output)


if __name__ == '__main__':
    print(Solution().main('AAABB'))