from typing import List

class Solution:
    def doesValidArrayExist(self, derived: List[int]) -> bool:
        res=0
        for i in derived:
            res^=i
        
        return res==0
        