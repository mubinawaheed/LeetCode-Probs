from collections import deque
from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows=len(isWater)
        cols=len(isWater[0])
        res=[]
        for i in range(rows):
            res.append([-1]*cols)
        
        q = deque()
        
        for r in range(rows):
            for c in range(cols):
                if isWater[r][c]:
                    q.append((r,c))
                    res[r][c]=0
                   
        while q:
            i,j=q.popleft()

            h= res[i][j]+1


            if( j-1 >= 0 and res[i][j-1] == -1):
                q.append((i,j-1))
                res[i][j-1] = h

            if (i+1 < rows  and res[i+1][j] == -1):
                q.append((i+1,j))
                res[i+1][j] = h 

            if (i-1 >=0  and res[i-1][j] == -1):
                q.append((i-1,j))
                res[i-1][j] = h 

            if (j+1<cols  and res[i][j+1] == -1):
                q.append((i,j+1))
                res[i][j+1] = h 
            
        return res