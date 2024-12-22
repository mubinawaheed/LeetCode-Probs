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