def getNeighbor(grid, r, c):
    R = len(grid)
    C = len(grid[0])
    sum = 0
    if 0 <= r - 1 < R and 0 <= c < C and grid[r - 1][c] == 1:
        sum += 1
    if 0 <= r < R and 0 <= c - 1 < C and grid[r][c - 1] == 1:
        sum += 1
    if 0 <= r + 1 < R and 0 <= c < C and grid[r + 1][c] == 1:
        sum += 1
    if 0 <= r < R and 0 <= c + 1 < C and grid[r][c + 1] == 1:
        sum += 1
    return sum


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        perimeter = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                perimeter += 4 - getNeighbor(grid, i, j)
        return perimeter