
from typing import Optional
# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        p1 = root.left
        p2=root.right

        def isSame(left,right):
            if(not right and not left):
                return True
            if((not right and left) or(not left and right)):
                return False
            if(left.val != right.val): # compare roots
                return False

            # now compare left child with right child
            return isSame(left.left, right.right) and isSame(left.right, right.left)
        return isSame(p1, p2)