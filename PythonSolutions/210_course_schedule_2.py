# 2021 May 19
from typing import List, Set, Tuple
# Topological sorting (topsort).
# The design involved in this dfs is, if the dependencies of a course
# are all visited, we consider a course viable. If any course gets into a cycle, meaning
# we add it in a set first, and if it shows up again as some prereq of prereq ,,,, the dfs
# returns a false and we return a [] in the main loop. If it's already visited, or all of 
# prereqs are fulfilled, we return True. But in the latter case, we add node as visited, and
# add it to the path, also remove it from the cycle set as it's dependencies are fulfilled.
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = {c: [] for c in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)

        path = []
        visited, cycle = set(), set()
        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False
            cycle.remove(course)
            visited.add(course)
            path.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return path

if __name__ == "__main__" :
    print(Solution().findOrder(1, []))
        