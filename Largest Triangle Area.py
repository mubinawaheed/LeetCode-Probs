from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        res=0
        n=len(points)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1, n):
                    res = max(res, 0.5*abs(

                        points[i][0]*(points[j][1] - points[k][1]) +
                        points[j][0]*(points[k][1] - points[i][1]) +
                        points[k][0]*(points[i][1] - points[j][1]) 
                    ))
        return res