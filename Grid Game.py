from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        n=len(grid[0])
        row1=grid[0].copy()
        row2=grid[1].copy()

        for i in range(1,n):
            row1[i]+=row1[i-1]
            row2[i]+=row2[i-1]

        res=float("inf")
        for i in range(n):
            top=row1[-1]-row1[i]
            bottom=row2[i-1] if i>0 else 0
            second=max(top, bottom)
            res=min(second,res)
        return res