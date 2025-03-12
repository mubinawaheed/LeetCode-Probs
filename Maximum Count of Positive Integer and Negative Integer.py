from typing import List


class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        n=len(nums)
        if nums[-1] < 0:
            return n
        count=0
        i=0
        while i<n and nums[i]<=0:
            if nums[i]<0:
                count+=1
            i+=1

        return max(count, n-i)