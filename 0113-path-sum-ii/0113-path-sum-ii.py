# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        result = []   # all valid paths found
        path = []     # current path from root to the node we're visiting

        def dfs(node, remaining):
            # Base case: nothing to explore
            if node is None:
                return

            # Step in: add this node to the current path
            path.append(node.val)

            # Leaf check: does the path end here with the right sum?
            if node.left is None and node.right is None and node.val == remaining:
                result.append(path[:])   # save a snapshot copy
            else:
                dfs(node.left, remaining - node.val)
                dfs(node.right, remaining - node.val)

            # Step out: backtrack so the parent sees its own path again
            path.pop()

        dfs(root, targetSum)
        return result