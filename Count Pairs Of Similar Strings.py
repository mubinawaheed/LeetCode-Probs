from typing import Counter, List

class Solution:
    def similarPairs(self, words: List[str]) -> int:
        # u=0
        # for i in range(len(words)-1):
        #     for j in range(i+1, len(words)):
        #         if (set(words[i]) == set(words[j])):
        #             u+=1
        # # return u

        s={}
        for i in words:
            c=Counter(i)
            p="".join(sorted(c.keys()))
            if p in s:
                s[p]+=1
            else:
                s[p]=1
        count=0
        for v in s.values():
            o=v*(v-1)//2
            count+=o
        return count