from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(9):
            s=set()
            for j in range(9):
                if board[i][j] =='.':
                    continue
                
                if board[i][j] in s:
                    return False
                else:
                    s.add(board[i][j])
                
        for i in range(9):
            s=set()
            for j in range(9):
                if board[j][i] =='.':
                    continue
                
                if board[j][i] in s:
                    return False
                else:
                    s.add(board[j][i])
                
        boxes = [(0,0), (0,3), (0,6),
        (3,0), (3,3), (3,6), (6,0), (6,3), (6,6)]

        for i, j in boxes:
            s=set()
            for r in range(i, i+3):
                
                for c in range(j, j+3):
                    if board[r][c] == '.':
                        continue
                    if board[r][c] in s:
                        return False
                    else:
                        s.add(board[r][c])
                

        return True




board =[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
print(Solution().isValidSudoku(board))

