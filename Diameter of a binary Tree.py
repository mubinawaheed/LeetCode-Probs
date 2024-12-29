# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        res=0
        def dfs(root):
            if not root:
                
                return 0

            l=dfs(root.left)
            f=dfs(root.right)
            nonlocal res
            res = max(res, l+f)
        
            return 1+max(l,f)
        dfs(root)
        return res
        