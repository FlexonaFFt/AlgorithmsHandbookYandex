# solution_stream.py
import sys
from collections import deque

def ints_from_stdin():
    # Потоковый генератор целых из stdin.buffer без создания большого списка
    for token in sys.stdin.buffer.read().split():
        yield int(token)

def main():
    it = ints_from_stdin()
    try:
        n = next(it)
    except StopIteration:
        print(0)
        return

    stack = deque([-1])  # индексы "открытий" (нечётных)
    best = 0
    i = 0

    # Обрабатываем числа по одному, не сохраняя весь список
    while i < n:
        x = next(it)
        if x & 1:  # нечётное — открытие
            stack.append(i)
        else:      # чётное — закрытие
            stack.pop()
            if not stack:
                # сброс базовой позиции
                stack.append(i)
            else:
                best = max(best, i - stack[-1])
        i += 1

    print(best)

if __name__ == "__main__":
    main()

