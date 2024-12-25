
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        m=head
        k=head
        length=0
        while head:
            length+=1
            head = head.next
        if length == 1:
            m = None
            return

        d= abs(length - n -1)

        if n == length:
            if(m.next):
                m=m.next
                return m
        i=0
        while i<d:
            i+=1
            m=m.next
        if m.next:
            m.next = m.next.next
            return k
        m.next = None
        return k
