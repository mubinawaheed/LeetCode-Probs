class Solution:
    def getDecimalValue(self, head) -> int:
        a=[]
        while head:
            a.append(str(head.val))
            head = head.next

        f=''.join(a)
        return int(f,2)