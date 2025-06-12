from typing import List


class Solution:
    def maxAdjacentDistance(self, nums: List[int]) -> int:
        s=0
        for i in range(len(nums)):
            a=0
            if i==len(nums)-1:
                a=nums[0]
            else:
                a=nums[i+1]
            s= max(s, abs(nums[i]-a))
        return s