from collections import Counter


class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if k>len(s):
            return False
        m= Counter(s)
        count=0
        for i in m.values():
            count+= 1 if i%2 !=0 else 0
        
        return count<=k