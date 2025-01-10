# Definition for a binary tree node.
import collections
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if(not root):
            return []
        q = collections.deque()
        q.append(root)
        res=[]
        while q:
            n=len(q)
            nodes=[]
            for i in range(n):
                node = q.popleft()
                nodes.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(sum(nodes)/len(nodes))
        return res
