# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        res=[]
        def traverse(root):
            if(root is None):
                return False
            res.append(root.val)
            traverse(root.left)
            uniV = all(ele == res[0] for ele in res)
            if(not uniV):
                return False

            traverse(root.right)
            return all(ele == res[0] for ele in res)

        return traverse(root)