# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.seen=set()

        def dfs(root, v):
            self.seen.add(v)

            if root.left:
                dfs(root.left, 2*v+1)
            
            
            if root.right:
                dfs(root.right, 2*v+2)
        dfs(root,0)

        

    def find(self, target: int) -> bool:

        return target in self.seen
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)