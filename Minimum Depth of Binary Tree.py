# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        lh=0
        rh=0
        if root is None:
            return 0
        # if(root.left is not None):
        lh = self.minDepth(root.left)
        # if(root.right is not None):
        rh = self.minDepth(root.right)
        if(root.left is None and root.right is None):
            return min(rh,lh)+1
        if(root.right is None):
            return lh+1
        if(root.left is None):
            return rh+1
        return min(lh,rh)+1