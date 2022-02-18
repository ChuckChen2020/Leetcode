# 2021 June 14 15:28 - June 15 11:27

# Constant memory means interim memory can be used.
# 1) Start with the four corners of any layer, swap them in the way that reflects
# the 90 degree rotation.
# 2) shift right, down, left, up one unit from the four respective points, and do
# the swapping.
# 3) Keep repeating it for n - 1 times, where n is the length of the edge of the # current layer.
from typing import List
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        dirs = (0, 1, 0, -1, 0)
        for r in range(N // 2):
            ind = [[r,r], [r, N-1-r], [N-1-r,N-1-r], [N-1-r,r]]
            for _ in range(r, N - 1 - r):
                for i in range(4):
                    ind[i][0] += dirs[i]
                    ind[i][1] += dirs[i+1]
                x1, y1 = ind[0]
                x2, y2 = ind[1]
                x3, y3 = ind[2]
                x4, y4 = ind[3]
                matrix[x1][y1], matrix[x2][y2], matrix[x3][y3], matrix[x4][y4]= matrix[x4][y4], matrix[x1][y1], matrix[x2][y2], matrix[x3][y3]
                

