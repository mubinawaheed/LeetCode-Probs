from typing import List


class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        res=0
        curr=0
        min_prev=0
        max_prev=0
        for i in range(len(nums)):
            curr+=nums[i]
            res=max(abs(curr-min_prev), abs(curr-max_prev), res)
            min_prev= min(min_prev, curr)
            max_prev= max(max_prev, curr)

        return res