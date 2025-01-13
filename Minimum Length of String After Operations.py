from typing import Counter


class Solution:
    def minimumLength(self, s: str) -> int:
        res=0
        for i in Counter(s).values():
            if i%2==0:
                res+=2

            else:
                res+=1
        return res
        