from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubPath(self, head: Optional[ListNode], root: Optional[TreeNode]) -> bool:
        if not head:
            return True
        if not root:
            return False

        if self.isSame(root, head):
            return True
        
        return self.isSubPath( head, root.left) or self.isSubPath( head,root.right)


    def isSame(self, root,head):
        if not head:
            return True
        if root and head and root.val == head.val:
            return self.isSame(root.left, head.next) or self.isSame(root.right, head.next)
        return False
    
tree= TreeNode(1)
tree.left = TreeNode(4)
tree.right = TreeNode(4)
tree.left.right = TreeNode(2)
tree.left.right.left = TreeNode(1)
tree.right.left = TreeNode(2)
tree.right.left.left = TreeNode(6)
tree.right.left.right = TreeNode(8)
tree.right.left.right.right = TreeNode(3)
tree.right.left.right.left = TreeNode(1)
k=ListNode(4)
k.next=ListNode(2)
k.next.next=ListNode(6)
s=Solution()
e=s.isSubPath(k, tree)
print(e)