from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        lh=0
        rh=0
        if root is None:
            return 0
        if(root.left is not None):
            lh = self.maxDepth(root.left)
        if(root.right is not None):
            rh = self.maxDepth(root.right)
        if lh>rh:
            return lh+1
        return rh+1
        