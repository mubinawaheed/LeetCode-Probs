from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        res=0
        curr=1
        start=0
        for i in range(1,len(nums)):
            if nums[i-1]<nums[i]:
                curr+=1
            else:
                curr=i
                res=max(res, sum(nums[start:curr]))
                start=i

        res=max(res, sum(nums[start:curr+1]))
        return res
    
s=Solution()
print(s.maxAscendingSum([5,5,6,6,6,9,1,2]))  # Output: