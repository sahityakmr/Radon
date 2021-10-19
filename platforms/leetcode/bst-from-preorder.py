from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        if len(preorder) == 0:
            return None
        root = TreeNode(preorder[0])
        k = 0
        found = False
        for i in range(1, len(preorder)):
            k = i
            if preorder[i] > preorder[0]:
                found = True
                break
        if not found:
            k = len(preorder)
        if len(preorder) > 1:
            if k > 1:
                root.left = self.bstFromPreorder(preorder[1:k])
            if k < len(preorder):
                root.right = self.bstFromPreorder(preorder[k:len(preorder)])
        return root


print(Solution().bstFromPreorder([4,2]))
