from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    order=[]
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res=[]
        def inOrder(root):
            if(root is None):
                return []
            if(root.left is not None):
                inOrder(root.left)
            res.append(root.val)
            if(root.right is not None):
                inOrder(root.right)
        
        inOrder(root)
        return res
        