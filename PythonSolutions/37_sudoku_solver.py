# 2021 May 9 14:49 surrendered.
from typing import List, Set, Tuple
import copy
# Don't know why the solution below doesn't work. The problem lies in the deepcopy, backtracking part.
# For each grid, exclude numbers in the row, col, and the subbox, check the remaining candidates, if the next node returns True it then returns True, which traces all the way to the top in the call stack, where the row number hits 9. Then the solution is found in all the 81 grids so it skips.
class Solution1:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        centers = [1,4,7]
        dirs = [-1,0,1]
        def search(board, r, c):
            if r == ROWS: return True            
            new_r, new_c = (r, c+1) if c != COLS - 1 else (r+1, 0)
            if board[r][c] != ".":
                return search(board, new_r, new_c)

            conflicts = set()
            for i in range(ROWS):
                x = board[i][c]
                if x != ".":
                    conflicts.add(x)
            for j in range(COLS):
                x = board[r][j]
                if x != ".":
                    conflicts.add(x)
            done = False
            for c_x in centers:
                for c_y in centers:
                    if abs(r - c_x) <= 1 and abs(c - c_y) <=1:
                        for dx in dirs:
                            for dy in dirs:
                                x = board[c_x + dx][c_y + dy]
                                if x != ".":
                                    conflicts.add(x)
                        done = True
                        break
                if done: break
            possibilities = [str(x) for x in range(1,10) if str(x) not in conflicts]
            print(r,c, possibilities)
            # This way will cause problem.
            cpy = copy.deepcopy(board)
            for poss in possibilities: 
                board[r][c] = poss
                if search(board, new_r, new_c): return True
                board = cpy
                #board[r][c] = '.'
            return False

        search(board, 0, 0)


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        def fill(board, row, col):
            if row == 9: return True
            new_row, new_col = (row, col+1) if col != 8 else (row+1, 0) 

            if board[row][col] != '.':
                return fill(board, new_row, new_col)

            for num in range(1,10):
                box_key = int(row/3)*3 + int(col/3)
                if not rows[row][num-1] and not cols[col][num-1] and not boxes[box_key][num-1]:
                    rows[row][num-1] = 1
                    cols[col][num-1] = 1
                    boxes[box_key][num-1] = 1
                    board[row][col] = str(num)
                    if fill(board, new_row, new_col):
                        return True
                    rows[row][num-1] = 0
                    cols[col][num-1] = 0
                    boxes[box_key][num-1] = 0
                    board[row][col] = '.'
            return False                     

        rows = [[0 for _ in range(9)] for _ in range(9)]
        cols = [[0 for _ in range(9)] for _ in range(9)]
        boxes = [[0 for _ in range(9)] for _ in range(9)]

        for r in range(9):
            for c in range(9):
                if board[r][c] != '.':
                    num = int(board[r][c])
                    rows[r][num - 1] = 1
                    cols[c][num - 1] = 1
                    boxes[int(r/3)*3 + int(c/3)][num - 1] = 1
        fill(board, 0, 0)

               
class Solution2:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        ROWS, COLS = len(board), len(board[0])
        centers = [1,4,7]
        dirs = [-1,0,1]
        def search(board, r, c):
            if r == ROWS:
                return True
            if board[r][c] != ".":
                if c < COLS - 1:
                    return search(board, r, c + 1)
                else:
                    return search(board, r + 1, 0)
            conflicts = set()
            for i in range(ROWS):
                x = board[i][c]
                if x != ".":
                    conflicts.add(x)
            for j in range(COLS):
                x = board[r][j]
                if x != ".":
                    conflicts.add(x)
            done = False
            for c_x in centers:
                for c_y in centers:
                    if abs(r - c_x) <= 1 and abs(c - c_y) <=1:
                        for dx in dirs:
                            for dy in dirs:
                                x = board[c_x + dx][c_y + dy]
                                if x != ".":
                                    conflicts.add(x)
                        done = True
                        break
                if done: break
            possibilities = [str(x) for x in range(1,10) if str(x) not in conflicts]

            # Such way of retracing the board would cause problem!
            # cpy = copy.deepcopy(board)     
            for poss in possibilities: 
                board[r][c] = poss
                if c < COLS - 1 and search(board, r, c + 1):
                    return True
                elif c == COLS - 1 and search(board, r + 1, 0):
                    return True
                #board = cpy
                board[r][c] = '.'
            return False
        search(board, 0, 0)


                                
                

if __name__ == "__main__":
    board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]
    Solution1().solveSudoku(board)
    print(board)
