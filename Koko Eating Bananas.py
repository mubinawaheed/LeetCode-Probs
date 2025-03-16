from math import ceil
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        def canEat(m):
            count=0
            for p in piles:
                count+=ceil(p/m)
                if count>h:
                    return False
                        
            return True
                
        
        l, r = 1, max(piles)

        res=0
        while l<=r:
            m= (l+r)//2

            if (canEat(m)):
                res=m
                r=m-1
            else:
                l=m+1
        return res


