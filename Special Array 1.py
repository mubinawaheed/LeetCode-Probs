from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True


        for i in range(1, len(nums)):
            b1 = nums[i-1] & 1
            b2 = nums[i] & 1
            if b1 == b2:
                return False
        return True

        
        