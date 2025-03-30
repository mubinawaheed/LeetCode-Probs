from collections import defaultdict
from typing import List

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        sp=defaultdict(int)
        for i, c in enumerate(s):
            sp[c] = i
        res=[]
        count=0
        end=0
        for i, c in enumerate(s):
            count+=1
            if sp[c] > end:
                end=sp[c]
            if end == i:
                res.append(count)
                count=0
        return res
p=Solution()
res=p.partitionLabels( "ababcbacadefegdehijhklij")
print(res)