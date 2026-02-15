"""
You are given a 2D matrix matrix of integers with R rows and C columns.

You start from any cell in the first column and move to the last column, one column at a time.

From a cell (row, col), you may move to:
        •	(row, col + 1)
        •	(row - 1, col + 1) (if row > 0)
        •	(row + 1, col + 1) (if row < R - 1)

The sharpness of a path is defined as the maximum value encountered along that path.

Your task is to compute the minimum possible sharpness among all valid paths from column 0 to column C - 1.

Return that minimum sharpness value.
"""


class SharpnessValue:
    def __init__(self, matrix):
        self.ROW = len(matrix)
        self.COL = len(matrix[0])
        self.res = []
        self.directions = [(0, 1), (-1, 1), (1, 1)]

    def dfs(self, r, c, max_value):
        max_value = max(max_value, self.matrix[r][c])

        if c == self.COL - 1:
            return max_value

        sharpness_values = []

        for d1, d2 in self.directions:
            new_r = d1 + r
            new_c = d2 + c

            if new_r >= 0 and new_c >= 0 and new_r < self.ROW and new_c <= self.COL:
                sharpness_values.append(self.dfs(new_r, new_c, max_value))

        return min(sharpness_values)

    def calculate_sharpness(self):
        for r in range(self.ROW):
            self.res.append(self.dfs(r, 0, float("-inf")))

        return min(self.res)
