def build_min_half(m, s):
    digits = []
    for i in range(m):
        for d in range(0 if i else 1, 10):
            remaining = s - d
            max_possible = 9 * (m - i - 1)
            if 0 <= remaining <= max_possible:
                digits.append(d)
                s = remaining
                break
    return digits

def build_max_half(m, s):
    digits = []
    for i in range(m):
        for d in range(9, (-1 if i else 0), -1):
            remaining = s - d
            max_possible = 9 * (m - i - 1)
            if 0 <= remaining <= max_possible:
                digits.append(d)
                s = remaining
                break
    return digits

def solve(K, S):
    m = K // 2
    best_min = None
    best_max = None

    for c in range(0, 10) if K % 2 else [0]:
        S2 = S - c
        if S2 < 0 or S2 % 2 != 0:
            continue
        half_sum = S2 // 2
        if half_sum < 0 or half_sum > 9 * m:
            continue
        if m == 0:
            # K == 1
            num = str(c)
            if best_min is None or int(num) < int(best_min):
                best_min = num
            if best_max is None or int(num) > int(best_max):
                best_max = num
            continue

        # минимальный
        left = build_min_half(m, half_sum)
        if left and left[0] != 0:
            left_str = ''.join(map(str, left))
            cand = left_str + (str(c) if K % 2 else '') + left_str[::-1]
            if best_min is None or int(cand) < int(best_min):
                best_min = cand

        # максимальный
        left = build_max_half(m, half_sum)
        if left and left[0] != 0:
            left_str = ''.join(map(str, left))
            cand = left_str + (str(c) if K % 2 else '') + left_str[::-1]
            if best_max is None or int(cand) > int(best_max):
                best_max = cand

    print(best_min, best_max)

# Ввод
K, S = map(int, input().split())
solve(K, S)
