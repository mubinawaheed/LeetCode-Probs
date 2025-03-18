from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res=0
        curr=0
        l=0
        # r=1
        # use OR to set bits and XOR to unset bits

        for r in range(len(nums)):
            
            while nums[r] & curr:
                curr = curr ^ nums[l]
                l+=1
            res=max(res, r-l+1)
            curr = curr | nums[r]


        return res
    
s=Solution()
s.longestNiceSubarray([1,3,8,48,10])