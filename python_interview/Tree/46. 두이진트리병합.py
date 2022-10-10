from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:

        # 내풀이
        def dfs(first, sec):
            if not sec:
                return

            if first.left:
                if sec.left and first.left != sec.left:
                    first.left.val += sec.left.val
            else:
                if sec.left:
                    first.left = sec.left
            if first.right:
                if sec.right and first.right != sec.right:
                    first.right.val += sec.right.val
            else:
                if sec.right:
                    first.right = sec.right

            dfs(first.left, sec.left)
            dfs(first.right, sec.right)

        if not root1 or not root2:
            return root1 or root2
        if root1 and root2:
            root1.val += root2.val
        dfs(root1, root2)
        return root1

        # 책
        if not root1 or not root2:
            return root1 or root2
        if root1 and root2:
            node = TreeNode(val = root1.val+root2.val)
            node.left = self.mergeTrees(root1.left, root2.left)
            node.right = self.mergeTrees(root1.right, root2.right)
            return node
