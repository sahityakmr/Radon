from typing import List


def search(board, r, c, word):
    for i in range(4)
    pass


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if search(board, i, j, word):
                        return True
        return False
