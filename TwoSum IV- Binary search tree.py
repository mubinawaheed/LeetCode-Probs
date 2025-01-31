# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        h=set()
        def dfs(root):
            if not root:
                return False

            if k - root.val in h:
                return True
            h.add(root.val)
            a=dfs(root.left)
            if not a:
                return dfs(root.right)
            return a

        return dfs(root)


        