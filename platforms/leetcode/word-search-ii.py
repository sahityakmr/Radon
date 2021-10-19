import collections
from typing import List

delta = [-1, 0, 1, 0, -1]


class Trie:
    def __init__(self):
        self.ends_here = False
        self.children = collections.defaultdict(Trie)

    def insert(self, word):
        node = self
        for w in word:
            node = node.children[w]
        node.ends_here = True


class Solution:
    def __init__(self):
        self.result = []
        self.trie = Trie()

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        for word in words:
            self.trie.insert(word)

        for i in range(len(board)):
            for j in range(len(board[0])):
                self.find(self.trie, board, i, j, [])
        return self.result

    def find(self, trie, board, i, j, word):
        if trie.ends_here is True:
            trie.ends_here = False
            self.result.append("".join(word))

        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        temp = board[i][j]

        trie = trie.children.get(temp)

        if not trie:
            return

        board[i][j] = '@'
        word.append(temp)

        self.find(trie, board, i + 1, j, word)
        self.find(trie, board, i - 1, j, word)
        self.find(trie, board, i, j + 1, word)
        self.find(trie, board, i, j - 1, word)

        word.pop()
        board[i][j] = temp
