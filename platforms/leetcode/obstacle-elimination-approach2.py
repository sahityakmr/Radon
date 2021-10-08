from typing import List
from collections import deque


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        gr = len(grid)
        gc = len(grid[0])
        if gr == gc == 1:
            return 0

        if k >= gr + gc - 2:
            return gr + gc - 2

        queue = deque([(0, 0, k, 0)])
        visited = {(0, 0, k)}

        while queue:
            r, c, power, steps = queue.popleft()
            for nr, nc in [(r - 1, c), (r, c - 1), (r + 1, c), (r, c + 1)]:
                if 0 <= nr < gr and 0 <= nc < gc:
                    if grid[nr][nc] == 1 and power > 0 and (nr, nc, power - 1) not in visited:
                        visited.add((nr, nc, power - 1))
                        queue.append((nr, nc, power - 1, steps + 1))
                    if grid[nr][nc] == 0 and (nr, nc, power) not in visited:
                        if nr == gr - 1 and nc == gc - 1:
                            return steps + 1
                        visited.add((nr, nc, power))
                        queue.append((nr, nc, power, steps + 1))
        return -1


print(Solution().shortestPath([[0, 0, 0],
                               [1, 1, 0],
                               [0, 0, 0],
                               [0, 1, 1],
                               [0, 0, 0]], 1))
print(Solution().shortestPath([[0, 1, 1],
                               [1, 1, 1],
                               [1, 0, 0]], 1))
print(Solution().shortestPath([[0, 1],
                               [1, 1],
                               [0, 0]], 1))
