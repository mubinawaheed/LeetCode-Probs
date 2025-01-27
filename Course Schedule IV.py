from collections import defaultdict
from typing import List


class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        maper = defaultdict(list)
        for i,j in prerequisites:
            maper[j].append(i)

        prereq={}

        def dfs(course):
            if course not in prereq:
                prereq[course]=set()
                for crs in maper[course]:
                    prereq[course] |= dfs(crs) #union of hashsets
                prereq[course].add(course)
            return prereq[course]


        for i in range(numCourses):
            dfs(i)
                

        res=[]
        for k in queries:
            q=prereq[k[1]]
            if(k[0] in q):
                res.append(True)
            else:
                res.append(False)

        return res