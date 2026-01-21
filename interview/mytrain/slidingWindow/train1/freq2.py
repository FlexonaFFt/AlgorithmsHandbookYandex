def longest_k_distinct(s: str, k: int) -> int:
    if k == 0:
        return 0
    freq = {}
    left = 0
    best = 0

    for right, ch in enumerate(s):
        # TODO 1: добавить ch в freq
        freq[ch] = freq.get(ch, 0) + 1

        # TODO 2: пока в окне больше k разных символов:
        #   - уменьшить freq для s[left]
        #   - если стало 0, удалить ключ
        #   - left += 1
        while len(freq) > k:
            out = s[left]
            freq[out] -= 1
            if freq[out] == 0:
                del freq[out]
            left += 1

        # TODO 3: обновить best
        best = max(best, right - left + 1)

    return best
