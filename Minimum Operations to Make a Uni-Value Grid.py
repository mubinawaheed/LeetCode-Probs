
from typing import List


class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        count = 0
        nums=[]
        remainder = grid[0][0] % x 
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if (remainder != grid[i][j]%x):
                    return -1
                nums.append(grid[i][j])
        
        num = self.median(nums)
        
        for k in nums:
            count+=( abs(num - k) // x)
        return count

    
    def median(self, lst):
        lst.sort()
        n = len(lst)
        mid = n // 2
        return lst[mid]
