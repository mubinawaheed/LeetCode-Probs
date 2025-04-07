from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool: # Memory limit exceeded:
        halfSum=sum(nums)//2
        if sum(nums)%2 != 0:
            return False
        cache={}
        def dfs(i, currSum):
            if (i, currSum) in cache:
                return cache[(i, currSum)]
            if i==len(nums) or currSum>halfSum:
                return False
            if currSum == halfSum:
                return True
            include = dfs(i + 1, currSum + nums[i])
            skip = dfs(i + 1, currSum)
            cache[(i, currSum)] = include or skip
            return cache[(i, currSum)]
            
        
        return dfs(0,0)
    
    def canPartition(self, nums: List[int]) -> bool: #Bottom-up DP solution
        halfSum=sum(nums)//2
        if sum(nums)%2 != 0:
            return False
        dp=set()
        dp.add(0)
        for i in range(len(nums)-1, -1, -1):
            nextDp = set()
            for t in dp:
                nextDp.add(t+nums[i])
                nextDp.add(t)
                if (t+nums[i] == halfSum):
                    return True
            dp=nextDp

        return False

s=Solution()
s.canPartition([2,2,2,2])