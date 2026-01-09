n = int(input())
string1 = str(input().strip())
string2 = str(input().strip())

result_parts = []
for i in range(n):
    result_parts.append(string1[i])
    result_parts.append(string2[i])

result = ''.join(result_parts)
print(result)
