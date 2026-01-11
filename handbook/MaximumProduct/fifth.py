class Solution:
    def main(self, array: list[int]):
        positives, negatives = [], []
        zeros, chosen_indices = [], []

        for i, x in enumerate(array, start=1):
            if x > 0: positives.append((abs(x), i))
            elif x < 0: negatives.append((abs(x), i))
            else: zeros.append(i)

        if positives or len(negatives) >= 2:
            chosen_indices.extend(idx for _, idx in positives)
            negatives.sort(reverse=True)
            if len(negatives) % 2 == 1: negatives.pop()

            for j in range(0, len(negatives), 2):
                chosen_indices.append(negatives[j][1])
                chosen_indices.append(negatives[j+1][1])

            if not chosen_indices:
                if zeros: chosen_indices = [zeros[0]]
                else:
                    max_idx = max(range(n), key=lambda k: array[k]) + 1
                    chosen_indices = [max_idx]

        else:
            if zeros: hosen_indices = [zeros[0]]
            else:
                max_idx = max(range(n), key=lambda k: array[k]) + 1
                chosen_indices = [max_idx]

        print(" ".join(map(str, chosen_indices)))


if __name__ == '__main__':
    n = int(input())
    nums = list(map(int, input().split()))
    solve = Solution()
    solve.main(nums)
