from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:   
        s=0
        def dfs(root):
            if(not root):
                return 0
            l=dfs(root.left)
            r=dfs(root.right)
            nonlocal s
            s+=abs(l-r)
            return root.val+l+r
            
        dfs(root)
        return s

        


