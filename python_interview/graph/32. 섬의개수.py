from collections import deque
from typing import List
in_range = lambda a, b: 0 <= a < r and 0 <= b < c

direc = [(-1, 0), (1, 0), (0, -1), (0, 1)]
r, c = 0, 0


def search(x, y, grid, visited):
    q = deque([(x, y)])
    while q:
        qx, qy = q.popleft()
        for d in direc:
            nx, ny = qx + d[0], qy + d[1]
            if in_range(nx, ny) and grid[nx][ny] == '1':
                if not visited[nx][ny]:
                    visited[nx][ny] = True
                    q.append((nx, ny))


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        global r, c

        count = 0
        r, c = len(grid), len(grid[0])
        visited = [[False] * c for _ in range(r)]
        for i in range(r):
            for j in range(c):
                if grid[i][j] == '1' and not visited[i][j]:
                    count += 1
                    visited[i][j] = True
                    search(i, j, grid, visited)

        return count


sol = Solution()
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]))