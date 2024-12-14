# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
from typing import Optional


#using floyds turtoise and hare algorithm - SLow - Fast pointer approach.
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False