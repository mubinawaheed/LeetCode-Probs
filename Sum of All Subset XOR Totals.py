from typing import List


class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        
        def dfs(i, res): # T(n) = 2^n
            if i == len(nums):
                return res
            return dfs(i+1, res^nums[i]) + dfs(i+1, res)

        return dfs(0,0)
    
    def subsetXORSum(self, nums: List[int]) -> int:
        
        res=0   #T(n) = O(n)
        for n in nums:
            res = res | n
        return res  << (len(nums) - 1)