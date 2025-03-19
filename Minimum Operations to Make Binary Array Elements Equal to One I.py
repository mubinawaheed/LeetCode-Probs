from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        res=0
        for r in range(len(nums)-2):
            if  nums[r] == 0:
                nums[r] ^=1
                nums[r+1] ^=1
                nums[r+2] ^=1
                res+=1
        if nums[-1] ==0 or nums[-2] == 0:
            return -1
        return res
            

nums =[0,1,1,1,0,0]
s=Solution()
print(s.minOperations(nums))  # Output: 2