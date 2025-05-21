from typing import List



class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None: # WORKS - but not optimized
        s = set()
        rows = len(matrix)
        cols = len(matrix[0])
        
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0 and (i, j) not in s:
                    # Mark all elements in the row as 0 and add them to set
                    for col in range(cols):
                        if matrix[i][col] != 0:
                            s.add((i, col))
                        matrix[i][col] = 0
                    
                    # Set top and bottom if in bounds
                    for row in range(rows):
                        if matrix[row][j] != 0:
                            s.add((row, j))
                        matrix[row][j] = 0

                    # Mark this zero too
                    s.add((i, j))

    def setZeroes(self, matrix: List[List[int]]) -> None: # OPTIMIZED - Much better
        rows = len(matrix)
        cols = len(matrix[0])
        zero_rows = set()
        zero_cols = set()

        # First pass: find all rows and columns that need to be zeroed
        for i in range(rows):
            for j in range(cols):
                if matrix[i][j] == 0:
                    zero_rows.add(i)
                    zero_cols.add(j)

        # Second pass: set cells to zero
        for i in range(rows):
            for j in range(cols):
                if i in zero_rows or j in zero_cols:
                    matrix[i][j] = 0

        
s=Solution()
matrix =[[0,1,2,0],[3,4,5,2],[1,3,1,5]]
s.setZeroes(matrix)
        