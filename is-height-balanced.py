# Definition for a binary tree node.
from typing import Optional

# A height-balanced binary tree is a binary tree in which the depth of the two subtrees of every node never differs by more than one.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool: # Time Complexity O(n)
        if (root is None ):
            return True
            
        def getHeight(node):
            if(node is None):
                return 0
            rh = 0
            lh = 0
            if (node.left is not None):
                lh = getHeight(node.left)
            if(node.right is not None):
                rh = getHeight(node.right)

            return 1 + max(rh, lh)
        
        r = getHeight(root.right)
        l = getHeight(root.left)
        result = r-l == 0 or r-l== 1 or r-l == -1
        if(result == False):
            return False

        result1 = True
        result2 = True
        if(root.left is not None):
            result1 = self.isBalanced(root.left)
        if(root.right is not None):
            result2 = self.isBalanced(root.right)

        return result1 and result2
    
    def isBalancedOptimized(self, root):  # Time complexity O(n2)
        def getHeight(node):
            if(node is None):
                return [True, 0]
            lh = getHeight(node.left)
            if(not lh[0]):
                return [False, lh[0]]
            
            rh = getHeight(node.right)
                
            res= (lh[0] and rh[0] )and (rh[1]-lh[1] ==0 or abs(rh[1]-lh[1]) ==1)
            
            return [res, 1 + max(rh[1], lh[1]) ]
        c= getHeight(root)
        return c[0]


# Explanation: The first checks for every node that if its height balanced or not. it calls DFS on every node . One node DFS = O(n) . So total time complexity is O(n2) for 1st solution. In the second solution i used a bottom up approach. During dfs only we dont just return depth of height but also check if the subtree is balanced. Therefore, we dont need to call dfs for every node. We'll just call DFS for root node and during DFS we are going to figure out if there is any subtree that is not balanced. Therefore, time complexity is O(n).