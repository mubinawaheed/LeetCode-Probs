from typing import List


class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        rows=len(grid)
        cols=len(grid[0])
        totalServers=0

        for i in range(rows):
            totalServers+=sum(grid[i])

        isolated=0
        for i in range(rows):
            k=sum(grid[i])
            if k > 1:
                continue
            if k == 1:
                
                for j in range(cols):
                    if grid[i][j] == 1:
                        col=j
                        f=0
                        for m in range(rows):
                            f+=grid[m][j]
                        if f==1:
                            isolated+=1
        return totalServers-isolated
  
s=Solution()
grid =[[1,0,0,1,0],[0,0,0,0,0],[0,0,0,1,0]]
print(s.countServers(grid)) #1