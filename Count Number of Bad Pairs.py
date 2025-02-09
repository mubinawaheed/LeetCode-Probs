from collections import defaultdict
from typing import List


class Solution:
    def countBadPairs(self, nums: List[int]) -> int:
        total=0
        goodPairs=0
        pairs=defaultdict(int)
        for i in range(len(nums)):
            total+=i
            goodPairs+=pairs[nums[i]-i]
            pairs[nums[i]-i]+=1

        return total-goodPairs