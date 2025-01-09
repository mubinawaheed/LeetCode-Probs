# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        def dfs(r1, r2):
            if not r1 and not r2:
                return None
            
            v1 = r1.val if r1 else 0
            v2 = r2.val if r2 else 0
            root = TreeNode(v1+v2)
            root.left = dfs(r1.left  if r1 else None, r2.left if r2 else None)
            root.right = dfs(r1.right if r1 else None, r2.right if r2 else None)
            return root
        res=dfs(root1, root2)
        return res
        