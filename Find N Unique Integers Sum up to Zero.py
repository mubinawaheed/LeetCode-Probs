from typing import List


class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n==1:
            return [0]

        res=[]
        for i in range(n):
            if len(res) == n:
                return res
            if i == 0 and n%2 == 0:
                continue
            if i == 0:
                res.append(i)
                continue
            res.append(-i)
            res.append(abs(i))

        return res