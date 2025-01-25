from collections import deque
from typing import List


class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups=[]
        mapp={}
        for i in sorted(nums):
            if len(groups) == 0 or abs(groups[-1][-1] - i) > limit:
                groups.append(deque())
            mapp[i] = len(groups)-1
            groups[-1].append(i)

        for n in range(len(nums)):
            nums[n]=groups[mapp[nums[n]]].popleft()

        return nums
