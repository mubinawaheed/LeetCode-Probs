from typing import List


class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        even=0
        odd=0
        a=str(bin(n)).replace("0b",'')
        a=a[::-1]
        for i in range(len(a)):
            if a[i] == '1':
                if i%2 ==0:
                    even+=1
                else:
                    odd+=1
        return [even, odd]
