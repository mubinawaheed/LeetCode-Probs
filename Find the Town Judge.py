from collections import defaultdict
from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        s=defaultdict(list)
        for i in range(len(trust)):
            m,o=trust[i]
            if m not in s:
                s[m] = []
            s[m].append(o)
        
        for i in range(1, n+1):
            c=0
            if i in s:
                continue
            for j in list(s.values()):
                if i in j:
                    c+=1
            if c == n-1 and (i not in s):
                return i

        return -1
