from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        res=[]
        for i in range(len(A)):
            m=A[0:i+1]
            n=B[0:i+1]            
            res.append(len(set(m) & set(n)))
        return res