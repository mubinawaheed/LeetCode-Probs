
from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        maxl=1
        res=1
        inc=0
        c=1
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                if inc>0:
                    c+=1
                else:
                    c=2
                    inc=1
            elif(nums[i-1]>nums[i]):
                if inc>0:
                    c=2
                    inc=-1
                else:
                    c+=1
            else:
                inc=0
                c=1
            res=max(res,c)
        return res