n, m = map(int, input().split())
print("Lose" if (n - m) % 3 == 0 else "Win")
