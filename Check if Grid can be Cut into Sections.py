from typing import List


class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        x= [(r[0], r[2]) for r in rectangles]
        y= [(v[1], v[3]) for v in rectangles]
        x.sort()
        y.sort()

        def count_intervals(interval):
            count=0
            prev=-1
            for s, e in interval:
                if prev <= s:
                    count+=1
                prev=max(prev, e)
            return count
        

        return max(count_intervals(x), count_intervals(y))>=3