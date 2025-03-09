from typing import List


class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        res=0
        left=0
        n=len(colors)
        for r in range(1,len(colors)+k-1):
            if colors[(r%n)-1] == colors[r%n]:
                left = r
            if r-left+1 > k:
                left+=1
            if r-left+1 == k:
                res+=1
        return res

