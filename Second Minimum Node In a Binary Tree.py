# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
from typing import Optional

class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        res=[]

        def dfs (root):
            if not root:
                return

            res.append(root.val)
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        if (len(set(res)) ==1):
            return -1

        sorted_list = sorted(set(res), reverse=True)
        return sorted_list[-2]

