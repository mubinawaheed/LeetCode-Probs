from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        numbers = list(range(0, len(nums)+1))
            
        missingNumber = sum(numbers)-sum(nums)
        return missingNumber