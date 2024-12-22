from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        

class Solution:
    def reverseList(self,head: Optional[ListNode]) -> Optional[ListNode]:
        p1=None
        p2=head
        while p2:
            currNext = p2.next
            p2.next = p1
            p1 = p2
            p2 = currNext
        return p1


