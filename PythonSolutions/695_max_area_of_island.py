# 2021 May 1, 19:29 - 20:01
from typing import List
def maxAreaOfIsland(grid: List[List[int]]) -> int:
        max_area = 0
        checked_indices = []
        rows = len(grid)
        cols = len(grid[0])

        def count_area(grid, row, col, checked_indices):
            if [row, col] in checked_indices or row in [-1, rows] or col in [-1, cols]:
                return 0
            else:
                checked_indices.append([row, col])

            if grid[row][col] == 0:
                return 0
            else:
                return 1 + count_area(grid, row -1, col, checked_indices) + count_area(grid, row +1, col, checked_indices) + count_area(grid, row, col - 1, checked_indices) + count_area(grid, row, col + 1, checked_indices)  
            
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, count_area(grid, row, col, checked_indices))

        return max_area

# The last solution was fine, but took 3124ms to pass all. The solution in the manual is slightly different yet more efficient in terms of memory accessing.  
def maxAreaOfIsland_1(grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])

        def count_area(grid, row, col):
            if row in [-1, rows] or col in [-1, cols] or grid[row][col] == 0:
                return 0
            else:
                # instead of keeping track of visited points, this solution sets 1 points back to 0, so that it won't be counted repeatedly. This avoids passing the list of checked points in the recursive calls, and greatly improved the speed.
                grid[row][col] = 0
                return 1 + count_area(grid, row -1, col) + count_area(grid, row +1, col) + count_area(grid, row, col - 1) + count_area(grid, row, col + 1)  
            
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, count_area(grid, row, col))

        return max_area        

# set does improves the solution a lot. Set seems to be quite a lot faster than list in checking existence. 
def maxAreaOfIsland_2(grid: List[List[int]]) -> int:
        max_area = 0
        checked_indices = set()
        rows = len(grid)
        cols = len(grid[0])

        def count_area(grid, row, col):
            if (row, col) in checked_indices or row in [-1, rows] or col in [-1, cols]:
                return 0
            else:
                checked_indices.add((row, col))

            if grid[row][col] == 0:
                return 0
            else:
                return 1 + count_area(grid, row -1, col) + count_area(grid, row +1, col) + count_area(grid, row, col - 1) + count_area(grid, row, col + 1)  
            
        for row in range(rows):
            for col in range(cols):
                max_area = max(max_area, count_area(grid, row, col))

        return max_area

# stack solution, this is the fastest.
def maxAreaOfIsland_stack(grid: List[List[int]]) -> int:
        max_area = 0
        rows = len(grid)
        cols = len(grid[0])
        dirs = [-1, 0, 1, 0, -1]
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    local_area = 1
                    grid[row][col] = 0
                    stack = []
                    stack.append([row, col])
                    while len(stack) != 0:
                        r, c = stack.pop() 
                        for i in range(4):
                            # Note that here r, c shouldn't be reused, because modifying them will alter the result for the next iteration.
                            rr = r + dirs[i]
                            cc = c + dirs[i+1]
                            if rr not in [-1, rows] and cc not in [-1, cols] and grid[rr][cc] == 1:
                                grid[rr][cc] = 0
                                local_area += 1
                                stack.append([rr, cc])
                    max_area = max(max_area, local_area)
        
        return max_area
                        



if __name__ == "__main__":
    print(maxAreaOfIsland_stack([[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]))