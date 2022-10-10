from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    longest = 0

    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        def dfs(now):
            if not now:
                return 0

            left = dfs(now.left)
            right = dfs(now.right)

            if now.left and now.left.val == now.val:
                left += 1
            else:
                left = 0

            if now.right and now.right.val == now.val:
                right += 1
            else:
                right = 0

            self.longest = max(self.longest, left + right)
            return max(left, right)
        dfs(root)
        return self.longest