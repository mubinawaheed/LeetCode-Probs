from collections import defaultdict
from sortedcontainers import SortedSet

class NumberContainers: # Got TLE Time limit Exceeded Error when using heap instead of sortedSet
   
    def __init__(self):
        self.container =defaultdict(SortedSet)
        self.indexes=defaultdict(int)

    def change(self, index: int, number: int) -> None:
        if index in self.indexes:
            v=self.indexes[index]
            self.container[v].remove(index)
  

        self.indexes[index]=number
        self.container[number].add(index)

        

    def find(self, number: int) -> int:
        if not self.container[number]:
            return -1
        return self.container[number][0]
        


obj = NumberContainers()
obj.change(1,10)
obj.change(1,10)
param_2 = obj.find(10)
obj.change(1,20)
param_3 = obj.find(10)
