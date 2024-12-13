# Definition for a binary tree node.
from typing import List, Optional

# Given the root of a binary search tree (BST) with duplicates, return all the mode(s) (i.e., the most frequently occurred element) in it.

# If the tree has more than one mode, return them in any order.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        res={}
        def dfs(root):
            if root is None:
                return
            if root.val in res:
                res[root.val]+=1
            else:
                res[root.val]=1
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        max_frequency = max(res.values())

        modes = [key for key, value in res.items() if value == max_frequency]


        return modes