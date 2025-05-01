from typing import List


class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        res=0
        for i in range(len(nums)):
            a=str(nums[i])
            if len(a) % 2 == 0:
                res+=1
        return res
        