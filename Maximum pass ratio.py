import heapq
from typing import List


class Solution:
    # pq=[]
    # def pushHeap(self,a,b,c):
    #     currentAvg = a/b
    #     newAvg = (a+1)/(b+1)
    #     diff=currentAvg - newAvg
    #     heapq.heappush(self.pq,(diff, c))

    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        pq=[]
        for i in range(len(classes)):
            # self.pushHeap(classes[i][0], classes[i][1], i)
            currentAvg = classes[i][0]/classes[i][1]
            newAvg = (classes[i][0]+1)/(classes[i][1]+1)
            diff=currentAvg - newAvg
            heapq.heappush(pq,(diff, i))

        n=len(classes)
        while extraStudents>0:
            diff, index = heapq.heappop(pq)
            classes[index][0]+=1
            classes[index][1]+=1
            heapq.heappush(pq, ((classes[index][0]/classes[index][1]-(classes[index][0]+1)/(classes[index][1]+1)), index))
            extraStudents-=1
            
        maxRatio=0
        for i in range(len(classes)):
            maxRatio+=classes[i][0]/classes[i][1]
        return maxRatio/n

        
            
s=Solution()
print(s.maxAverageRatio([[1,2],[3,5],[2,2]], 2))