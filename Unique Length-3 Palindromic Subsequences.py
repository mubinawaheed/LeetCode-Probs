from typing import Counter


class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left=set()
        right=Counter(s)
        res=set()

        for i in s:
            right[i]-=1

            for c in left:
                if right[c]>0:
                    res.add((c,i))

            left.add(i)


        return len(res)
        