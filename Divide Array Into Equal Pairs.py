from typing import Counter, List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:

        c=Counter(nums)

        for i in c.values():
            if i%2 != 0:
                return False
        return True
