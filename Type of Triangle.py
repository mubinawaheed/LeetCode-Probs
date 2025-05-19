from typing import Counter, List


class Solution:
    def triangleType(self, nums: List[int]) -> str:

        s=Counter(nums)

        if (len(s.keys())==1):
            return "equilateral"
        nums.sort()

        if nums[-1] >= nums[0]+nums[1]:
            return "none"
        if (len(s.keys())==2):
              return "isosceles"
        return 'scalene'
        
        
class Solution:
    def triangleType(self, nums: List[int]) -> str:

        nums.sort()

        if (nums[0]==nums[2]):
            return "equilateral"
        if nums[-1] >= nums[0]+nums[1]:
            return "none"
        if (nums[0]==nums[1] or nums[2]==nums[1]):
              return "isosceles"
        return 'scalene'