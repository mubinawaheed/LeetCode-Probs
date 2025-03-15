from typing import List


class Solution:
    def minCapability(self, nums: List[int], k: int) -> int:
            
        def check( m):
            i=0
            res=0
            while i<len(nums):
        
                if nums[i] <= m:
                    res+=1
                    i+=2
                else:
                    i+=1

                if res==k:
                    return True
            return False
            
        l, r= min(nums), max(nums)
        res=0
        while l<=r:
            m = (l+r)//2

            if check(m):
                res=m
                r=m-1
            else:
                l=m+1
        return res

