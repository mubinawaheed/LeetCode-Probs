from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int:
        res=0
        visited=set()
        waterCells={}
        rows=len(grid)
        cols=len(grid[0])

        def dfs(i,j):
            if (i<0 or i==rows or j==cols or j<0 or (i,j) in visited) or grid[i][j]==0:
                return 0
   
            res=grid[i][j]
            visited.add((i,j))
            if( j-1 >= 0):
                res+=dfs(i, j-1)
                
            if (i+1 < rows ):
                res+=dfs(i+1, j)
               
            if (i-1 >=0 ):
                res+=dfs(i-1, j)
                
             
            if (j+1<cols):
                res+=dfs(i, j+1)
                
            return res


        for r in range(rows):
            for c in range(cols):
                if grid[r][c] > 0:
                    waterCells[(r,c)] = grid[r][c]
                    res=max(res, dfs(r,c))

  
        return res


              