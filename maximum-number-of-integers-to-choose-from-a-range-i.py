from typing import List

# maximum-number-of-integers-to-choose-from-a-range-i

class Solution: 
    # looking up in SET is of constant time
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        selected = []
        s=set(banned)
        for i in range(1, n+1):
            if((sum(selected)+i)>maxSum):
                break
            if i in s:
                continue
            selected.append(i)

        return len(selected)