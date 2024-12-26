from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp={}
        def recursion(i, total):
            if i == len(nums):
                return 1 if total == target else 0
            if (i, total) in dp:
                return dp[(i, total)]
            dp[(i, total)] = recursion(i+1, total+nums[i]) + recursion(i+1, total-nums[i])
            return dp[(i,total)]
        return recursion(0,0)