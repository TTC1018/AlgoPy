from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        def dfs(now):
            if not now:
                return -1

            left, right = dfs(now.left), dfs(now.right)

            sum_val = left + right + 2
            self.longest = max(self.longest, sum_val)
            return max(left, right) + 1

        dfs(root)
        return self.longest
    