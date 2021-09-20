from typing import List


class Solution:

    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[-1 for i in range(3)] for j in range(3)]
        player = 0
        for i, j in moves:
            player = player ^ 1
            grid[i][j] = player
        i, j = moves[-1]
        if grid[0][j] == grid[1][j] == grid[2][j] == player or grid[i][0] == grid[i][1] == grid[i][2] == player or \
                grid[0][0] == grid[1][1] == grid[2][2] == player or grid[0][2] == grid[1][1] == grid[2][0] == player:
            if player == 1:
                return "A"
            return "B"
        if len(moves) < 9:
            return "Pending"
        return "Draw"


res = Solution().tictactoe([[0, 0], [1, 1], [0, 1], [0, 2], [1, 0], [2, 0]])
print(res)
