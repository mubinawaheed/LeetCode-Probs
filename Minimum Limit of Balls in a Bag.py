

from typing import List


def minimumSize( nums: List[int], maxOperations: int) -> int:
    for i in range(maxOperations):
        maxE=max(nums)
        if(maxE%2 == 0):
            nums.remove(maxE)
            nums.append(maxE//2)
            nums.append(maxE//2)
        else:
            ops = maxOperations
            lst=list(range(1, maxE+1))
            low=0
            high=len(lst)-1
            mid=None
            while low<high and ops>0:
                mid = (low+high)//2
                high = mid
                ops-=1
            a1 = lst[mid]
            a2 = abs(maxE-a1)
            index = nums.index(maxE)
            del nums[index]
            nums.append(a1)
            nums.append(a2)
    return max(nums)

print(minimumSize([9], 2))