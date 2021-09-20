from typing import List


def checkWinner(grid, i, j, player) -> bool:
    # check row win
    won = True
    for k in range(3):
        if grid[i][k] != player:
            won = False
            break
    if won:
        return True

    # check col win
    won = True
    for k in range(3):
        if grid[k][j] != player:
            won = False
            break
    if won:
        return True

    # check diagonal one
    won = True
    for k in range(3):
        if grid[k][k] != player:
            won = False
            break
    if won:
        return True

    # check diagonal two
    won = True
    for k in range(3):
        if grid[k][2 - k] != player:
            won = False
            break
    if won:
        return True
    return False


class Solution:

    def tictactoe(self, moves: List[List[int]]) -> str:
        grid = [[-1 for i in range(3)] for j in range(3)]
        player = 1
        for i, j in moves:
            grid[i][j] = player
            if checkWinner(grid, i, j, player):
                if player == 1:
                    return "A"
                return "B"
            player = player ^ 1
        if len(moves) < 9:
            return "Pending"
        return "Draw"

