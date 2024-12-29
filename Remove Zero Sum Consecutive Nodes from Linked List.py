
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        count=0
        p=head
        s={}
        while p:
            count+=p.val
            if count in s:
                node = s[count]
                node.next = p.next
                while list(s.keys())[-1] != count:
                    s.popitem()
            elif count == 0:
                head = p.next
                s={}
            else:
          
                s[count] = p
            p=p.next
        return head
        
        
a=ListNode(2)
a.next=ListNode(2)
a.next.next=ListNode(-2)
a.next.next.next=ListNode(1)
a.next.next.next.next=ListNode(-1)
a.next.next.next.next.next=ListNode(-1)


s=Solution()
l=s.removeZeroSumSublists(a)
print(l)