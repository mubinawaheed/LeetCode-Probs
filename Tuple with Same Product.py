from collections import defaultdict
from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        s=defaultdict(int)
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                k=nums[i]*nums[j]
                s[k]+=1
        res=0
        for key,val in s.items():
    
            res+= (val * (val - 1) // 2) * 8
        return res

        