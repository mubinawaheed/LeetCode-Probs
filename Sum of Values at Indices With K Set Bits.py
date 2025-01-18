from typing import List


class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        sum=0
        for i in range(len(nums)):
            if (self.count_set_bits(i)==k):
                sum+=nums[i]
        return sum
        
    def count_set_bits(self,n):
        return bin(n).count('1')