from typing import List


class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        k=''
        for i in range(len(spaces)):
            k+=s[len(k)-i:spaces[i]]+' '
        k+=s[len(k)-len(spaces):]
        return k
