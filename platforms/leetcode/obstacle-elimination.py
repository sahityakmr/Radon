from typing import List
import queue


class Solution:

    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        gr = len(grid)
        gc = len(grid[0])
        if gr == gc == 1:
            return 0
        ops = [[[False, -1, -1] for i in range(gc)] for j in range(gr)]
        ops[0][0] = [False, 0, k]

        q = queue.Queue()
        q.put([0, 0])

        delta = [-1, 0, 1, 0, -1]

        while not q.empty():
            r, c = q.get()
            ops[r][c][0] = True
            for i in range(4):
                nr = r + delta[i]
                nc = c + delta[i + 1]

                if nr == gr - 1 and nc == gc - 1:
                    return ops[r][c][1] + 1

                if 0 <= nr < gr and 0 <= nc < gc and ops[nr][nc][0] is False:
                    loss = 0
                    if grid[nr][nc] == 1:
                        loss = 1
                    if ops[r][c][2] >= loss:
                        ops[nr][nc] = [False, ops[r][c][1] + 1, ops[r][c][2] - loss]
                        q.put([nr, nc])
        return -1


# print(Solution().shortestPath([[0, 0, 0],
#                                [1, 1, 0],
#                                [0, 0, 0],
#                                [0, 1, 1],
#                                [0, 0, 0]], 1))
# print(Solution().shortestPath([[0, 1, 1],
#                                [1, 1, 1],
#                                [1, 0, 0]], 1))
print(Solution().shortestPath([[0, 1],
                               [1, 1],
                               [0, 0]], 1))
