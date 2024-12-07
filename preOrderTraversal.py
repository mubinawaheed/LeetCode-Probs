# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    
    def preorderTraversal(self, root):
        res=[]
        def t(root):
            if(root is None):
                return []
            res.append(root.val)
            t(root.left)
            t(root.right)
            return res
        return t(root)