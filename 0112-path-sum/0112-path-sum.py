# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root, targetSum):
        # Case 1: empty node, no path here
        if root is None:
            return False

        # Case 2: leaf node, check if the remaining target matches
        if root.left is None and root.right is None:
            return root.val == targetSum

        # Case 3: try both subtrees with the reduced target
        remaining = targetSum - root.val
        return (self.hasPathSum(root.left, remaining) or
                self.hasPathSum(root.right, remaining))