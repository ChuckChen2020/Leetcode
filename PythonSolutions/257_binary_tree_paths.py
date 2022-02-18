# 2021 May 6, 23:47 - 00:12
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        stack = [root]
        prev = dict()
        ans = []
        def retrieve_path(end, start, prev):
            path = []
            pt = end
            while True:
                path.append(str(pt.val))
                if pt == start: break
                pt = prev[pt]
            path.reverse()
            return "->".join(path)
        
        while len(stack)!= 0:
            node = stack.pop()
            if node.left: 
                stack.append(node.left)
                prev[node.left] = node
            if node.right:
                stack.append(node.right)
                prev[node.right] = node
            if node.left is None and node.right is None:
                ans.append(retrieve_path(node, root, prev))
        return ans

if __name__ == "__main__":    
    print(Solution().binaryTreePaths([1,2,3,None,5]))