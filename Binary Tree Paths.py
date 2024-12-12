# Definition for a binary tree node.
# Given the root of a binary tree, return all root-to-leaf paths in any order.

# A leaf is a node with no children.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        res=[]
        value=''
        def getPaths(root, value):
            if(root is None):
                return
            value+=str(root.val)+'->'
            if(root.left is None and root.right is None):
                res.append(value[0:len(value)-2])
            getPaths(root.left, value)
            getPaths(root.right, value)

        getPaths(root, value)
        return res