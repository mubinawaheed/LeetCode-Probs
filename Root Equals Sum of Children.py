# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        v=0
        if(root.right is not None):
            v+=root.right.val
        if(root.left is not None):
            v+=root.left.val
        return v==root.val