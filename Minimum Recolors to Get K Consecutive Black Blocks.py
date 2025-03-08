from typing import Counter


class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        recolors = k
        left=0
        while right<len(blocks):
            s=Counter(blocks[left: right+1])
            recolors = min(recolors, s['W'])
            left+=1
            right+=1
        return recolors
    
    def minimumColors(self, blocks,k): # optimized
    
        recolors = k
        left=0
        c=0
        for i in range(len(blocks)):
            if blocks[i] == 'W':
                c+=1
            if i-left+1 == k:
                recolors=min(c, recolors)
                if blocks[left]=='W':
                    c-=1
                left+=1
                
        return recolors