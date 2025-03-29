# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        p=head
        dummy = ListNode(0, head)
        prev= dummy
        curr=head
        while curr and curr.next:
            sec = curr.next
            nextPair = curr.next.next
            sec.next = curr 
            curr.next = nextPair
            prev.next = sec

            prev=curr
            curr=curr.next
            
        
        
        return dummy.next