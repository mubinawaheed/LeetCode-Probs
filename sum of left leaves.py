# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        self.total=0
        def dfs(root, isLeft):
            if root is None:
                return
            if(root.left is None and root.right is None and isLeft):
                self.total+=root.val
            dfs(root.left, True)
            dfs(root.right, False)
        dfs(root, False)
        return self.total
        