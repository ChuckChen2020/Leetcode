# 2021 May 2, 03:46 - 04:31
from typing import List
# Darn slow. I guess memoizing the connectivity of visited points to the two sets of boundaries can reduce some repetitions.
def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [-1,0,1,0,-1]
        ret = []
        for row in range(rows):
            for col in range(cols):
                stack = []
                visited = set()
                stack.append([row, col])
                connectPacific = connectAtlantic = False

                while len(stack) != 0:
                    r,c = stack.pop()

                    if r == 0 or c == 0:
                        connectPacific = True

                    if r == rows - 1 or c == cols - 1:
                        connectAtlantic = True
                        
                    if connectAtlantic and connectPacific:
                        ret.append([row, col])
                        break

                    for i in range(4):
                        x = r + dirs[i]
                        y = c + dirs[i+1]
                        if x not in [-1, rows] and y not in [-1, cols] and heights[x][y] <= heights[r][c] and (x,y) not in visited:
                            stack.append([x,y])
                    
                    visited.add((r,c))

        return ret

# From the boundaries to points. Then use the intersection of the two sets.
def pacificAtlantic_2(heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def stack_search(heights, i, j, connected_set):
            stack = [[i,j]]
            visited = {(i,j)}
            connected_set.add((i,j))
            dirs = [-1,0,1,0,-1]
            while len(stack) != 0:
                r, c = stack.pop()
                for k in range(4):
                    x = r + dirs[k]
                    y = c + dirs[k+1]
                    if x > -1 and x < len(heights) and y > -1 and y < len(heights[0]) and r > -1 and r < len(heights) and c > -1 and c < len(heights[0]) and heights[x][y] >= heights[r][c] and (x,y) not in visited:
                        stack.append([x,y])
                        visited.add((x,y))
                        connected_set.add((x,y))

        pac_set = set()
        atl_set = set()
        for col in range(cols):
            stack_search(heights, 0, col, pac_set)
            stack_search(heights, rows - 1, col, atl_set)
        for row in range(rows):
            stack_search(heights, row, 0, pac_set)
            stack_search(heights, row, cols - 1, atl_set)

        return list(map(lambda x: [x[0], x[1]], pac_set.intersection(atl_set)))        

# From the boundaries to points. Then use the intersection of the two sets.
def pacificAtlantic_2_recursion(heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        def dfs(heights, i, j, connected_set, visited):
            visited.add((i,j))
            connected_set.add((i,j))
            dirs = [-1,0,1,0,-1]

            for k in range(4):
                x = i + dirs[k]
                y = j + dirs[k+1]
                if x > -1 and x < len(heights) and y > -1 and y < len(heights[0]) and i > -1 and i < len(heights) and j > -1and j < len(heights[0]) and heights[x][y] >= heights[i][j] and (x,y) not in visited:
                    dfs(heights, x, y, connected_set, visited)

        pac_set = set()
        for col in range(cols):
            dfs(heights, 0, col, pac_set, set())
        for row in range(rows):
            dfs(heights, row, 0, pac_set, set())

        atl_set = set() 
        for col in range(cols):
            dfs(heights, rows - 1, col, atl_set, set())
        for row in range(rows):
            dfs(heights, row, cols - 1, atl_set, set())

        return list(map(lambda x: [x[0], x[1]], pac_set.intersection(atl_set)))

# BFS seem to yield correct solution, but TLE.
from collections import deque
def pacificAtlantic_bfs(heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])
        dirs = [-1,0,1,0,-1]
        ret = []
        for row in range(rows):
            for col in range(cols):
                queue = deque()
                visited = set()
                queue.append([row, col])
                connectPacific = connectAtlantic = False

                while len(queue) != 0:
                    r,c = queue.popleft()

                    if r == 0 or c == 0:
                        connectPacific = True

                    if r == rows - 1 or c == cols - 1:
                        connectAtlantic = True
                        
                    if connectAtlantic and connectPacific:
                        ret.append([row, col])
                        break

                    for i in range(4):
                        x = r + dirs[i]
                        y = c + dirs[i+1]
                        if x not in [-1, rows] and y not in [-1, cols] and heights[x][y] <= heights[r][c] and (x,y) not in visited:
                            queue.append([x,y])
                    
                    visited.add((r,c))

        return ret

# The recursion way might be hard, wasn't able to get it right.
# def pacificAtlantic_recursion(heights: List[List[int]]) -> List[List[int]]:
#     visited_pac = set()
#     visited_atl = set()
    
#     def more_to_try(heights, i, j, visited):
#         dirs = [-1, 0, 1, 0, -1]
#         for k in range(4):
#             x = i + dirs[k]
#             y = j + dirs[k+1]
#             if x not in (-1, len(heights)) and y not in (-1, len(heights[0])) and (x,y) not in visited and heights[x][y] <= heights[i][j]:
#                 return True
#         return False

    
#     def dfs_pac(heights, x, y, visited_pac):
#         if x == 0 or y == 0:
#             return True
#         elif x in (-1, len(heights)) or y in (-1, len(heights[0])) or (x,y) in visited_pac or not more_to_try(heights, x, y, visited_pac):
#             return False
#         else:
#             visited_pac.add((x,y))
#             return dfs_pac(heights, x - 1, y, visited_pac) or dfs_pac(heights, x + 1, y, visited_pac) or dfs_pac(heights, x, y - 1, visited_pac) or dfs_pac(heights, x, y + 1, visited_pac)

    
#     def dfs_atl(heights, x, y, visited_atl):
#         if x == len(heights) - 1 or y == len(heights[0]) - 1:
#             return True
#         elif x in (-1, len(heights)) or y in (-1, len(heights[0])) or (x,y) in visited_atl or not more_to_try(heights, x, y, visited_atl):
#             return False
#         else:
#             visited_atl.add((x,y))
#             return dfs_atl(heights, x - 1, y, visited_atl) or dfs_atl(heights, x + 1, y, visited_atl) or dfs_atl(heights, x, y - 1, visited_atl) or dfs_atl(heights, x, y + 1, visited_atl)

#     ret = []
#     for row in range(len(heights)):
#         for col in range(len(heights[0])):
#             if dfs_atl(heights, row, col, visited_atl) and dfs_pac(heights, row, col, visited_pac):
#                 ret.append([row, col])
#     return ret






if __name__ == "__main__":
    print(pacificAtlantic([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(pacificAtlantic_2([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(pacificAtlantic_2_recursion([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))
    print(pacificAtlantic_bfs([[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]))