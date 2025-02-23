
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not preorder:
            return None
        
        stack = []
        root = TreeNode(preorder[0])
        stack.append(root)

        preIndex, postIndex = 1, 0

        while stack:
            current = stack[-1]

            if current.val == postorder[postIndex]:
                stack.pop()
                postIndex += 1
            else:
                newNode = TreeNode(preorder[preIndex])
                preIndex += 1

                if current.left is None:
                    current.left = newNode
                else:
                    current.right = newNode

                stack.append(newNode)

        return root
