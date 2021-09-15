from collections import deque
from typing import List


class ZeroOneMatrix:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        rows, cols = len(mat), len(mat[0])
        queue = deque([])

        directions = [0, 1, 0, -1, 0]

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    queue.append((row, col))
                else:
                    mat[row][col] = -1

        while queue:
            row, col = queue.popleft()
            for i in range(4):
                nr, nc = row + directions[i], col + directions[i + 1]
                if nr < 0 or nr == rows or nc < 0 or nc == cols or mat[nr][nc] != -1:
                    continue
                mat[nr][nc] = 1 + mat[row][col]
                queue.append((nr, nc))
        return mat
