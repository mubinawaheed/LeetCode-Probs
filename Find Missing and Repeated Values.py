from collections import defaultdict
from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        s=defaultdict(int)
        res=[]
        repeatedElem=0
        for i in grid:
            for j in i:
                s[j]+=1
                if s[j]>1:
                    repeatedElem=j
 
        n=len(s.keys())+1
        sum_of_natural_nums = (n*(n+1))//2 #10
        return [repeatedElem,   sum_of_natural_nums - sum(s.keys())]
        
        
s=Solution()
s.findMissingAndRepeatedValues([[9,1,7],[8,9,2],[3,4,6]])