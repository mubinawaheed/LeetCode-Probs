from collections import defaultdict
from typing import List


class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        res=0
        diagnols = defaultdict(int)
     
        for i in range(len(dimensions)):
            l, w = dimensions[i][0] , dimensions[i][1]
            d = (l*l) + (w*w)
            diagnols[d]= max(l*w,  diagnols[d])


        return diagnols[max(diagnols.keys())]