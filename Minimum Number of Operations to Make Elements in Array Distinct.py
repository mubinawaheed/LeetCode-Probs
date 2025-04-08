from typing import List


class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res=0
        i=0
        while len(nums)>0:
            if len(nums) == len(set(nums)):
                return res
            
            res+=1
            for k in range(3):
                if len(nums)==0:
                    return res
                del nums[i]
                
        return res
    
    def minimumOperations(self, nums): #optimized
        mpp = [0] * 101
        for i in range(len(nums) - 1, -1, -1):
            mpp[nums[i]] += 1
            if mpp[nums[i]] == 2:
                return (i + 3) // 3
        return 0
s=Solution()
s.minimumOperations([2,2,13])