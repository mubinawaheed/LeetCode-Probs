# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        borrow=0
        dummy=ListNode(0)
        node=dummy
        while l1 or l2 or borrow:

            a1 = l1.val if l1 else 0
            a2 = l2.val if l2 else 0

            ans= a1 + a2 + borrow
            borrow = ans//10
            node.next=ListNode(ans%10)
           
            node=node.next

            if l1:
                l1=l1.next
            if l2:
                l2=l2.next
        
       
        return dummy.next
            
        