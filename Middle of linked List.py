# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        q=head
        while q:
            q=q.next

            if q:
                q=q.next
            else:
                break
            
            p= p.next
        return p