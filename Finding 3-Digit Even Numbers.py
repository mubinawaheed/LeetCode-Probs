from collections import defaultdict
from typing import Counter, List


class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:
        res=[]
        c=Counter(digits)
    
        for i in range(100, 999,2):
            if self.isValid(i,c):
                res.append(i)
        return res

    
    def isValid(self, x,c):
        num=x
        numss=defaultdict(int)
        while num>0:
            p=num%10
            if (p not in c) or (numss[p]>=c[p]):
                return False
            numss[p]+=1
            num=num//10
        return True