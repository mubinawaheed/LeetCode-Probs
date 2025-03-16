from typing import List


class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:

        def check(m):
            count=0
            for i in range(len(ranks)):
                count += int(sqrt(m/ranks[i]))
                if count >= cars:
                    return True
            return False
        
        
        
        l, r = 1, max(ranks)*cars*cars

        res=0
        while l<=r:
            m= (l+r)//2

            if (check(m)):
                res=m
                r=m-1
            else:
                l=m+1
        return res


