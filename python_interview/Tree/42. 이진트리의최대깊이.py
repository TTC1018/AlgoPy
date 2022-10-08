from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        answer = 0

        if root.val is not None:
            q = deque([(root, 1)])

            while q:
                now, depth = q.popleft()
                answer = depth

                if now.left:
                    q.append((now.left, depth + 1))
                if now.right:
                    q.append((now.right, depth + 1))

        return answer

