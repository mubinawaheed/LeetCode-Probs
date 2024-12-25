# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        res=[]
        
        def dfs(root, val):
            if not root:
                return
            
            v=f"{val}{root.val}"
            
            if(root.left is None and root.right is None):
                res.append(int(v, 2))
                
            dfs(root.left, v)
            dfs(root.right,v)
        
        dfs(root, '')

        return sum(res)

            

        