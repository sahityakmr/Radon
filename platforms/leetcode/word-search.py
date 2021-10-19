from typing import List

delta = [-1, 0, 1, 0, -1]


def search(board, r, c, word) -> bool:
    if len(word) == 0:
        return True
    for i in range(4):
        nr, nc = r + delta[i], c + delta[i + 1]
        if 0 <= nr < len(board) and 0 <= nc < len(board[0]) and board[nr][nc] == word[0]:
            temp = board[nr][nc]
            board[nr][nc] = '@'
            res = search(board, nr, nc, word[1:])
            if res:
                return True
            board[nr][nc] = temp
    return False


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    temp = board[i][j]
                    board[i][j] = '@'
                    if search(board, i, j, word[1:]):
                        return True
                    board[i][j] = temp
        return False


print(Solution().exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))
