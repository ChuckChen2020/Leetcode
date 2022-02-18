# 2021 May 1, 23:20 - 00:46.
# THe problem is essentially the same with the old problem 547 friend circles.

from typing import List, Set
def findCircleNum(isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        circles = 0
        visited = set()
        col = 0
        # if jumping to a row or a col is needed, using while loop might
        # gives you better flexibility.  
        while col < cols:
            if col in visited:
                col += 1
                continue

            stack = []
            row = col + 1
            while row < rows:
                if isConnected[row][col] == 1:
                    stack.append(row)
                    while len(stack) != 0:
                        c = stack.pop()
                        if c in visited:
                            continue
                        # DFS or BFS?
                        for r in range(rows):
                            if isConnected[r][c] == 1 and r not in [c, row]:
                                stack.append(r)
                        visited.add(c)
                row += 1
            circles += 1
            col += 1
        
        return circles

# The above solution is effectively dfs also. But to make it clearer, we can load the connected points in the stack, then pop the last element and process it again.
def findCircleNum_1(isConnected: List[List[int]]) -> int:
        rows = len(isConnected)
        cols = len(isConnected[0])
        circles = 0
        visited = set()
        col = 0
        while col < cols:
            if col in visited:
                col += 1
                continue

            stack = []
            row = col + 1
            while row < rows:
                if isConnected[row][col] == 1 and row not in visited:
                    stack.append(row)
                row += 1

            while len(stack) != 0:
                c = stack.pop()
                if c in visited:
                    continue
                else:
                    for r in range(rows):
                        if isConnected[r][c] == 1 and r != c and r not in visited:
                            stack.append(r)
                    visited.add(c)
            circles += 1
            col += 1
        
        return circles

#Recursion is easier for this problem.
def findCircleNum_recursion(isConnected: List[List[int]]) -> int:
        def dfs(isConnected: List[List[int]], row: int, visited: Set[int]) -> None:
            visited.add(row)
            for col in range(len(isConnected[0])):
                if isConnected[row][col] == 1 and col not in visited:
                    dfs(isConnected, col, visited)

        visited = set()
        count = 0
        for row in range(len(isConnected)):
            if row not in visited:
                dfs(isConnected, row, visited)
                count += 1
        return count 



if __name__ == "__main__":
    print(findCircleNum_recursion([[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]))