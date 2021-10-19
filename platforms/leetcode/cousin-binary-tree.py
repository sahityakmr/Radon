# Definition for a binary tree node.
import collections
import queue
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def depth(node):
    if node is None:
        return 0
    return 1 + max(depth(node.left), depth(node.right))


class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        to_search = {x, y}
        q = queue.Queue()
        q.put(root)
        process = []
        while not q.empty():
            temp_q = queue.Queue()
            while not q.empty():
                elem = q.get()
                if elem.left is not None:
                    temp_q.put(elem.left)
                    if elem.left.val in to_search:
                        to_search.remove(elem.left.val)
                        process.append((elem.left, elem))
                if elem.right is not None:
                    temp_q.put(elem.right)
                    if elem.right.val in to_search:
                        process.append((elem.right, elem))
                        to_search.remove(elem.right.val)
            if len(to_search) == 1:
                return False
            if len(to_search) == 0:
                # if process[0][1] == process[1][1]:
                #     return False
                # print(process[0][1].val, process[0][0].val, depth(process[0][0]))
                # print(process[1][1].val, process[1][0].val, depth(process[1][0]))
                # return depth(process[0][0]) == depth(process[1][0])
                return not process[0][1] == process[1][1]
            q = temp_q
        return False