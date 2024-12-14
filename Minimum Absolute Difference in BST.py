# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    min_value=float('inf')

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        res=[]
        def dfs(root):
            if root is None:
                return
            res.append(root.val)
            dfs(root.left)
            dfs(root.right)
        dfs(root)
        res = sorted(res)
        
        min_diff = float('inf')
        pair = (None, None)
    
        for i in range(len(res) - 1):
            diff = abs(res[i + 1] - res[i])
            if diff < min_diff:
                min_diff = diff
                pair = (res[i], res[i + 1])
        
        return abs(pair[0]-pair[1])
        

        