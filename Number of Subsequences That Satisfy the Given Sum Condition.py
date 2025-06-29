from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        res=0
        r=len(nums)-1
        for i in range(len(nums)):
            while nums[r]+nums[i]>target and i<=r:
                r-=1
            if(i<=r):
                res+=2**(r-i)
        return res % ((10**9) + 7)