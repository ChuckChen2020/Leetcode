#2021 May 4, 16:35 - 00:29
# Mutability of lists caused much trouble. Also should have swapped row and col.
from typing import List, Set, Tuple
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        def next_valid(queens: List[int])->List[int]:
            col_next = len(queens)
            ans = []

            for row_next in range(n):
                valid = True
                for col, row in enumerate(queens):
                    if (row_next == row or col_next == col or
                    abs(row_next - row) == abs(col_next - col)):
                        valid = False
                        break
                if valid: ans.append(row_next)
            return ans

        def next_step(queens: List[int], ans):
            choices = next_valid(queens)

            for x in choices:
                queens.append(x)
                if len(queens) == n:
                    ans.append(queens[:])
                else:
                    next_step(queens, ans)
                queens.pop()
            return

        def translate(ans:List[List[int]]):
            res = []
            for coords in ans:
                coords_dict = dict()
                for col, row in enumerate(coords):
                    coords_dict[row] = col
                sol = []    
                for row in range(n):
                    string = ''
                    for col in range(n):
                        if col == coords_dict[row]:
                            string += "Q"
                        else:
                            string += "."
                    sol.append(string)
                res.append(sol)
            return res

        if n == 1: return [["Q"]]
        first_queen = 0
        ans = []
        while first_queen < n:
            new_ans = []
            next_step([first_queen], new_ans)
            ans.extend(new_ans)
            first_queen += 1

        return translate(ans)





if __name__ == "__main__":
    print(Solution().solveNQueens(1))