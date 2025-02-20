from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n=len(nums[0])

        for i in range(2**n):
            if(bin(i)[2:].zfill(n) not in nums):
                return bin(i)[2: ].zfill(n)
        

        