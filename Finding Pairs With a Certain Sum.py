from typing import Counter, List


class FindSumPairs:
    
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.a1=nums1
        self.a2=nums2
        self.counter= Counter(nums2)

    def add(self, index: int, val: int) -> None:
        old=self.a2[index]
        self.counter[old]-=1
        self.a2[index]+=val
        self.counter[self.a2[index]]+=1

    def count(self, tot: int) -> int:
        ans=0
        for i in self.a1:
            if tot-i in self.counter:
                ans+=self.counter[tot-i]
        return ans


# Your FindSumPairs object will be instantiated and called as such:
# obj = FindSumPairs(nums1, nums2)
# obj.add(index,val)
# param_2 = obj.count(tot)