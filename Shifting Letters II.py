from typing import List


class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        shif = [0]*(len(s)+1)
        
        for left, right, direction in shifts:
            shif[right+1] += 1 if direction else -1
            shif[left] += -1 if direction else 1

        diff=0
        res=[ord(c)-ord("a") for c in s]
        for i in reversed(range(len(shif))):
            diff+=shif[i]
            res[i-1]=(diff+res[i-1])%26

        s=[chr(ord("a")+n) for n in res]
        return "".join(s)