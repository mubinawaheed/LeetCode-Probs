from typing import List


class Solution:
    
    # TLE error not accepted
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=0
        for i in range(len(nums)-1):            
            if(sum(nums[0: i+1]) >= sum(nums[-(len(nums)-i-1): ]) ):
                count+=1
        return count
    
    # Accepted Array
    def waysToSplitArray(self, nums: List[int]) -> int:
        count=0
        left=0
        right=sum(nums)
        for i in range(len(nums)-1):
            left +=nums[i]
            right -=nums[i]
            if left>=right:
                count+=1
        return count
        
        
a=Solution()
l=a.waysToSplitArray([10,4,-8,7])
print(l)