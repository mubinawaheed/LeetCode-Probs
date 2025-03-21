from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        count=0
        i=0
        while i<len(nums):
            if nums[i] == 0:
                del nums[i]
                count+=1
            else:
                i+=1
        nums.extend([0] * count)

s = Solution()
nums=[0,0,1]
s.moveZeroes(nums)
        