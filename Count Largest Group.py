from collections import defaultdict


class Solution:
    def countLargestGroup(self, n: int) -> int:
        if n<=9:
            return n
        res = 0
        groups = defaultdict(int)

        for i in range(1, n+1):
            sm = self.getSumOfDigits(i)
            groups[sm]+=1

        v=max(groups.values())
        for k in groups.values():
            if k == v:
                res+=1
        return res



    def getSumOfDigits(self,x):
        p=0
        while x>0:
            p+=x%10
            x=x//10
        return p