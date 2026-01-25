'''
Дано: матрица m x n, где:
строки отсортированы,первый элемент строки > последнего
элемента предыдущей строки.
Найти: есть ли target в матрице.
'''


class Search:
    def search_matrix(self, matrix: list[list[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])
        top, bottom, row = 0, m - 1, -1

        # сначала найду строку где может быть target
        while top <= bottom:
            mid = (top + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][n - 1]:
                row = mid
                break
            if target < matrix[mid][0]:
                bottom = mid - 1
            else: top = mid + 1

        # поиск внутри найденной строки
        if row == -1: return False
        left, right = 0, n - 1
        while left <= right:
            mid = (left + right) // 2
            val = matrix[row][mid]

            if val == target:
                return True
            if val < target:
                left = mid + 1
            else: right = mid - 1
        return False


if __name__ == '__main__':
    print(Search().search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 3))
    print(Search().search_matrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]], 13))
