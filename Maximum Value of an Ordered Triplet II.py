from typing import List
#MEDIUM

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        res=0
        n=len(nums)
        left=nums[0]
        maxDiff=0
        for j in range(n):
            res=max(res, maxDiff* nums[j])
            maxDiff = max(maxDiff, left-nums[j])
            left = max(left, nums[j])
        return res