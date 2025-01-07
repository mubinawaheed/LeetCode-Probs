from typing import List


def minOperations(boxes: str) -> List[int]:
    res=[]
    for i in range(len(boxes)):
        moves=0
        for j in range(len(boxes)):
            if i == j:
                continue
            if boxes[j] == '1':
                moves+=abs(j-i)
        res.append(moves)
    return res

a=minOperations('110')
print(a)