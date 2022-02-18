# 2021 May 3, 16:34 - 19:04 surrendered.
# Can't get the iterative stack solution to work. The visited status seems pretty hard to manage. 
from typing import List, Set, Tuple
# class Solution:
#     def exist(self, board: List[List[str]], word: str) -> bool:
#         def search_neighbors(board: List[List[str]], row:int, col:int, word: str):
#             stack = [[row,col，1]]            
#             dirs = [-1,0,1,0,-1]
#             path = set()

#             while len(stack) != 0:
#                 r,c,idx = stack.pop()
#                 path.add((r,c))
#                 some_points_fit = False
#                 for i in range(4):
#                     x = r + dirs[i]
#                     y = c + dirs[i+1]                    
#                     if x not in [-1, len(board)] and y not in [-1, len(board[0])] and word[idx] == board[x][y] and (x,y) not in path:
#                         some_points_fit = True
#                         if idx == len(word) - 1:
#                             return True
#                         else:
#                             stack.append([x,y,idx + 1])
                
#             return False

        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == word[0] and (len(word) == 1 or search_neighbors(board, row, col, word)):
                    return True
        return False

#Direct translation from Huahua's C++ solution.
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def search(board: List[List[str]], word: str, d:int, row:int, col:int)->bool:
            if row in [-1, len(board)] or col in [-1, len(board[0])] or word[d] != board[row][col]:
                return False
            if d == len(word) - 1:
                return True
            cur_copy = board[row][col]
            board[row][col] = 0
            found = (search(board, word, d+1, row+1, col) or 
                    search(board, word, d+1, row-1, col) or 
                    search(board, word, d+1, row, col+1) or 
                    search(board, word, d+1, row, col-1))
            board[row][col] = cur_copy
            return found

        ROWS, COLS = len(board), len(board[0])

        for row in range(ROWS):
            for col in range(COLS):
                if search(board, word, 0 , row, col):
                    return True
        return False            

if __name__ == "__main__":
    print(Solution().exist([["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]], "ABCESEEEFS"))