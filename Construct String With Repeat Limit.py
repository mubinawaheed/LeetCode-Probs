import heapq
from typing import Counter
# Construct String With Repeat Limit - Leetcode 2182

def repeatLimitedString(s: str, repeatLimit: int) -> str:
    h=[]
    count= Counter(s)
    for i, j in count.items():
        heapq.heappush(h, (-ord(i), j))
        
    l=[]
    
    while h:

        val, cnt= heapq.heappop(h) #('a',3) limit 3
        minv= min(cnt, repeatLimit)
        
        l.append(chr(-val)*minv)
        if(cnt - minv > 0 and h): #still some elements left
            a, nxt_cnt= heapq.heappop(h)
            l.append(chr(-a))
            if (nxt_cnt>1):
                heapq.heappush(h, (a, cnt-1))
            
            heapq.heappush(h, (val, nxt_cnt-minv))
            
    return "".join(l)

a=repeatLimitedString("cczazcc",3)
print(a)