from collections import defaultdict
from typing import List


class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        res=0
        d=defaultdict(int)
        for i in answers:
            if i ==0:
                res+=1
                continue
            d[i]+=1
            if d[i] == i+1:
                res+= d[i]
                d[i]=0

        for k, v in d.items():
            if v>0:
                res+=k+1

        return res
    
s=Solution()
s.numRabbits([0,0,1,1,1])