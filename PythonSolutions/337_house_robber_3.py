# 2021 May 25 08:17 - 09:18
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# DFS + Memoization (without memoization, TLE)
from functools import lru_cache
class Solution:
    def rob(self, root: TreeNode) -> int:
        @lru_cache(maxsize=None)
        def dfs(node, p_used):
            if node is None: return 0
            if not p_used:
                value_use = node.val + dfs(node.left, True) + dfs(node.right, True)
                value_not_use = dfs(node.left, False) + dfs(node.right, False)
                return max(value_use, value_not_use)
            else:
                return dfs(node.left, False) + dfs(node.right, False)
        return dfs(root, False)


# One thing that was done wrong in the beginning:
# Don't know what's wrong yet. It seems that the leaves are traversed but never be counted.
from functools import lru_cache
class Solution:
    def rob(self, root: TreeNode) -> int:
        def dfs(node, p_used):
            if not p_used:
                value_use = node.val + dfs(node.left, True) if node.left else 0 + dfs(node.right, True) if node.right else 0
                value_not_use = dfs(node.left, False) if node.left else 0 + dfs(node.right, False) if node.right else 0
                return max(value_use, value_not_use)
            else:
                return dfs(node.left, False) if node.left else 0+ dfs(node.right, False) if node.right else 0
        return dfs(root, False)

