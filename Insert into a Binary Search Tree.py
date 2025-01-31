# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional


class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root: 
            return TreeNode(val)
        def dfs(root):
            print(val)
            if val > root.val:
                if not root.right:
                    root.right = TreeNode(val)
                    return root
                else:
                    dfs(root.right)

            elif root.val>val:
                if not root.left:
                    root.left = TreeNode(val)
                    return root
                dfs(root.left)

        dfs(root)
        return root