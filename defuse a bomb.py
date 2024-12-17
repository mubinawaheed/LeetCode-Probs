from typing import List


class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        arr=[]
        for i in range(len(code)):
            if k == 0:
                return [0]*len(code)
            elif(k>0):
                a1=code[i+1:k+i+1]
                a2 = code[0: k- len(a1)]
                arr.append( sum(a1) + sum(a2))
            else:
               
                arr.append(sum(code[(i + j) % len(code)] for j in range(k, 0)))
        return arr
