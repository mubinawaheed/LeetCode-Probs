from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        res=[]
        d=defaultdict(int)
        for w in words2:
            count=Counter(w)
            for k, c in count.items():
                d[k] = max(c, d[k])

        for i in range(len(words1)):
            f = dict(Counter(words1[i]))
            if(self.are_pairs_in_dict(d, f)):
                res.append(words1[i])

        return res

    def are_pairs_in_dict(self,d1, d2):
        for key, value in d1.items():
            # Check if the key exists in d2 and has the same value
            if key not in d2 or d2[key] < value:
                return False
        return True

  

        