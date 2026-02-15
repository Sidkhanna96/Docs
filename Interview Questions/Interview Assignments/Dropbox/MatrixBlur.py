# Matrix Blur Operation
# Problem: Given a matrix, replace each element with the average of itself and its neighbors.


class Blur:
    def __init__(self, matrix):
        self.matrix = matrix
        self.ROW = len(matrix)
        self.COL = len(matrix[0])

    def _getAverage(self, r, c):
        self.directions = [
            (1, 0),
            (0, 1),
            (-1, 0),
            (0, -1),
            (1, -1),
            (-1, 1),
            (1, 1),
            (-1, -1),
        ]
        total = 0
        count = 0

        for d1, d2 in self.directions:
            newR = d1 + r
            newC = d2 + c

            if newR >= 0 and newC >= 0 and newR < self.ROW and newC < self.COL:
                total += self.matrix[newR][newC]
                count += 1

        total += self.matrix[r][c]

        return total / count

    def blur(self):
        self.grid = [[c for c in range(self.COL)] for r in range(self.ROW)]

        for r in range(self.ROW):
            for c in range(self.COL):
                self.grid[r][c] = self._getAverage(r, c)

        return self.grid
