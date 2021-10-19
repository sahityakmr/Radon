# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.dim = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.get_max(root)
        return self.dim

    def get_max(self, node):
        if node is None:
            return 0
        left = self.get_max(node.left)
        right = self.get_max(node.right)
        self.dim = max(self.dim, left + right)
        return 1 + max(left, right)
