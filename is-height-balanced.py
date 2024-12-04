# Definition for a binary tree node.
from typing import Optional

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if (root is None ):
            return True
            
        def getHeight(node):
            if(node is None):
                return 0
            rh = 0
            lh = 0
            if (node.left is not None):
                lh = getHeight(node.left)
            if(node.right is not None):
                rh = getHeight(node.right)
            if(lh>rh):
                return lh+1
            return rh+1
        
        r = getHeight(root.right)
        l = getHeight(root.left)
        result = r-l == 0 or r-l== 1 or r-l == -1
        if(result == False):
            return False

        result1 = True
        result2 = True
        if(root.left is not None):
            result1 = self.isBalanced(root.left)
        if(root.right is not None):
            result2 = self.isBalanced(root.right)

        return result1 and result2

