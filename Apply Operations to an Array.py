from typing import List


class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        count_of_zeros=0
        for i in range(len(nums)-1):
            if nums[i] == 0:
                count_of_zeros+=1
            if nums[i] == nums[i+1]:
                nums[i]=nums[i]*2
                nums[i+1]=0
        if nums[-1] == 0:
            count_of_zeros+=1

        while 0 in nums:
            k=nums.index(0)
            del nums[k]
        return nums + [0]*count_of_zeros