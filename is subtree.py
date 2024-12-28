# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot:
            return True
        if not root:
            return False
        if self.isSame(root,subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
        

    def isSame(self,mainTree, subTree):
        if not mainTree and not subTree:
            return True
        if mainTree and subTree and mainTree.val == subTree.val:
            return self.isSame(mainTree.left, subTree.left) and self.isSame(mainTree.right, subTree.right)
        return False