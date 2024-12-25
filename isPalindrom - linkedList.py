# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals=[]
        while head:
            vals.append(head.val)
            head = head.next
            
        r,l = 0, len(vals)-1
        while r<=l:
            if vals[r]!=vals[l]:
                return False
            r+=1
            l-=1
        return True