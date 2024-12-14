# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        while p is not None and p.next is not None:
            if p.val == p.next.val:
                p.next = p.next.next
            else:
                p=p.next
        return head
        
c= ListNode(1)
c.next=ListNode(1)
c.next.next=ListNode(2)

s= Solution()
h=s.deleteDuplicates(c)