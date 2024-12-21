# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
import collections
from typing import List, Optional


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if(not root):
            return []
        q = collections.deque()
        q.append(root)
        res=[]
        while q:
            n= len(q)
            childs=[]
            for i in range(n):
                node = q.popleft()
                if(node):
                    childs.append(node.val)
                    q.append(node.left)
                    q.append(node.right)
            if len(childs)>0:
                res.append(childs)
                
        return res
    
t=TreeNode(3)
t.left=TreeNode(9)
t.right=TreeNode(20)
t.right.left=TreeNode(15)
t.right.right=TreeNode(7)

s=Solution()
a=s.levelOrder(t)
print(a)