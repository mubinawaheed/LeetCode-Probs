from typing import List
class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        p={}
        
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                p[mat[i][j]]=[i,j]
        
        row_count=[0]*len(mat)
        col_count=[0]*len(mat[0])
        for i in range(len(arr)):
            r,c=p[arr[i]]
            col_count[c]+=1
            row_count[r]+=1

            if row_count[r] == len(mat[0]) or col_count[c] == len(mat):
                return i
            
