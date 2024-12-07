from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        currentSum=0
        def dfs(root,currentSum):
            if(root is None):
                return False
            currentSum+=root.val
            if(root.left is None and root.right is None and currentSum==targetSum):
                return True
            return dfs(root.left,currentSum) or dfs(root.right,currentSum)
        return dfs(root, currentSum)