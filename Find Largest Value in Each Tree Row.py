# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if(not root):
            return []
        q = collections.deque()
        q.append(root)
        maxE=[]
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
                maxE.append(max(childs))
        return maxE
        
