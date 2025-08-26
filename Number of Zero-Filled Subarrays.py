from typing import List


class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        behind_zero_count=0
        res=0
        for i in range(len(nums)):
            if nums[i] == 0:
                res +=(behind_zero_count+1)
                behind_zero_count+=1
            else:
                behind_zero_count=0
        return res