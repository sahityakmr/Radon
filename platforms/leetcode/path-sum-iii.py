# Definition for a binary tree node.
import collections
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.hashmap = collections.defaultdict(lambda : 0)
        self.targetSum = 0

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        self.targetSum = targetSum
        if root is None:
            return 0
        self.hashmap[0] = 1
        return self.count(root, 0)

    def count(self, node, sum_yet):
        sum_yet += node.val
        c = self.hashmap[sum_yet - self.targetSum]
        initial = self.hashmap[sum_yet]
        self.hashmap[sum_yet] = initial + 1
        if node.left is not None:
            c += self.count(node.left, sum_yet)
        if node.right is not None:
            c += self.count(node.right, sum_yet)
        initial = self.hashmap[sum_yet]
        self.hashmap[sum_yet] = initial - 1
        return c


root = TreeNode(10, TreeNode(5, TreeNode(3, TreeNode(3, None, None), TreeNode(-2, None, None)),
                             TreeNode(2, None, TreeNode(1, None, None))), TreeNode(-3, None, TreeNode(11, None, None)))
print(Solution().pathSum(root, 8))
