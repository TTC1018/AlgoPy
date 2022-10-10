from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(now):
            if not now:
                return

            now.left, now.right = now.right, now.left
            dfs(now.left)
            dfs(now.right)

        dfs(root)
        return root