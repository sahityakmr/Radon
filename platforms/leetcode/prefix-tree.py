

class TrieNode:
    def __init__(self):
        self.ends_here = False
        self.children = [None] * 26


def insert(node, word):
    if len(word) == 0:
        node.ends_here = True
    else:
        if node.children[ord(word[0]) - 97] is None:
            node.children[ord(word[0]) - 97] = TrieNode()
        insert(node.children[ord(word[0]) - 97], word[1:])


def search(node, word):
    if len(word) == 0:
        return node.ends_here is True
    else:
        if node.children[ord(word[0]) - 97] is None:
            return False
        return search(node.children[ord(word[0]) - 97], word[1:])


def startsWith(node, word):
    if len(word) == 0:
        if node.ends_here is True:
            return True
        for child in node.children:
            if child is not None:
                return True
        return False
    else:
        if node.children[ord(word[0]) - 97] is None:
            return False
        return startsWith(node.children[ord(word[0]) - 97], word[1:])


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        insert(self.root, word)

    def search(self, word: str) -> bool:
        return search(self.root, word)

    def startsWith(self, prefix: str) -> bool:
        return startsWith(self.root, prefix)