# 5. Island Problems & Graph Traversal
# Problem: Find the largest island and various follow-ups.


def findLargest(grid):
    ROW, COL = len(grid), len(grid[0])

    visited = set()

    def dfs(r, c):
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        size = 1
        visited.add((r, c))

        for d1, d2 in directions:
            newR = d1 + r
            newC = d2 + c

            if (
                newR >= 0
                and newC >= 0
                and newR < ROW
                and newC < COL
                and grid[newR][newC] == 1
                and (newR, newC) not in visited
            ):
                size += dfs(newR, newC)

        return size

    maxSize = 0

    for r in range(ROW):
        for c in range(COL):
            if grid[r][c] == 1 and (r, c) not in visited:
                count = 0
                dfs(r, c)
                maxSize = max(maxSize, count)

    return maxSize


from collections import defaultdict
import deque


## Find minimum flips to connect all Islands
class island:
    def __init__(self, matrix):
        self.islandId = 65
        self.islandCoordinates = defaultdict(set)  # {A: {(1,2), (4,5)}}
        self.islandMaxDist = defaultdict(list)  # {A: [2,6,1]}

    def _idGenerator(self):
        newId = ord(self.islandId)
        self.islandId += 1

        return newId

    def numberOfIsland(self, grid):
        self.ROW, self.COL = len(grid), len(grid[0])

        def dfs(r, c, islandId):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            grid[r][c] = islandId
            self.islandCoordinates[islandId].add((r, c))

            for d1, d2 in directions:
                newR = d1 + r
                newC = d2 + c

                if (
                    newR >= 0
                    and newC >= 0
                    and newR < self.ROW
                    and newC < self.COL
                    and grid[newR][newC] == 1
                ):
                    self.dfs(newR, newC, islandId)

        def bfs(islandId, r, c):
            directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

            queue = deque([r, c])

            while queue:
                curR, curC = queue.popleft()

                for d1, d2 in directions:
                    newR = curR + d1
                    newC = curC + d2

                    if newR >= 0 and newR < self.ROW and newC >= 0 and newC < self.COL:
                        if grid[newR][newC] == 0:
                            grid[newR][newC] += 1
                            queue.append((newR, newC))
                            break

                        if (
                            grid[newR][newC] != islandId
                            and grid[newR][newC] in self.islandCoordinates
                        ):
                            self.islandMaxDist[grid[newR][newC]].append(
                                grid[curR][curC]
                            )
                            break

        for r in range(self.ROW):
            for c in range(self.COL):
                if grid[r][c] == 1:
                    islandId = self._idGenerator()

                    dfs(r, c, islandId)

        for keyIslandId in self.islandCoordinates:
            for r, c in self.islandCoordinates[keyIslandId]:
                bfs(keyIslandId, r, c)

        minFlip = 0
        for key in self.islandMaxDist:
            minFlip += min(self.islandMaxDist[key])

        return minFlip
