# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        a,b=0,0
        p, q = headA, headB
        while p is not None:
            a+=1
            p=p.next
        while q is not None:
            b+=1
            q=q.next
        p,q = headA, headB
        if a>b:
            diff=a-b
            while diff > 0:
                p=p.next
                diff-=1
        elif(a<b):
            diff = b-a
            while diff > 0:
                q=q.next
                diff-=1
        while p and q:
            if p == q:
                return p
            p=p.next
            q=q.next
        return
