from collections import defaultdict
from typing import Counter, List


class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        left = defaultdict(int)
        right = Counter(nums)
        n=len(nums)
        print(left, right)
        for i in range(len(nums)):
            left[nums[i]]+=1
            right[nums[i]]-=1
            if left[nums[i]] * 2 > i+1 and right[nums[i]] * 2 > n-i-1:
                return i
        return -1
    
    def minimumIndex(self, nums): # optimized using boyer voting algorithm
        majority=0
        count=0
 
        for n in nums:
            if count == 0:
                majority = n
                
            if majority==n:
                count+=1
            else:
                count-=1
        left = 0
        right = nums.count(majority)
        
        for i in range(len(nums)):
            if nums[i] == majority:
                left+=1
                right -=1
            if left*2 > i+1 and right*2 > len(nums)-i-1:
                return i