import math
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        s={}
        for  i in range(len(nums)):
            if nums[i] in s:
                s[nums[i]]+=1
            else:
                s[nums[i]]=1
        for k, j in s.items():
            if j  >= math.ceil(len(nums)/2):
                return k
            
            
    def majorityElement(self, nums: List[int]) -> int: # optimized

        s={}
        for n in nums:
            s[n] = s.get(n,0)+1
            if s[n]>maxV:
                res = n
            maxV = max(maxV, s[n])
        return res
    
    def majorityElement(self, nums): # Boyer-Moore Voting Algorithm
        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
                
            if res==n:
                count+=1
            else:
                count-=1
        return res