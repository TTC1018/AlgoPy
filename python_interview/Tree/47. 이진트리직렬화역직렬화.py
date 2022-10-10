from collections import deque


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root:TreeNode) -> str:
        result = ['#']

        q = deque()
        if root:
            q.append(root)

            while q:
                now = q.popleft()
                if not now:
                    result.append('#')
                    continue
                result.append(now.val)
                q.append(now.left)
                q.append(now.right)

        return ' '.join(map(str, result))

    def deserialize(self, data:str) -> TreeNode:
        if data == '#':
            return


        data = data.split()
        root = TreeNode(int(data[1]))
        index = 2
        q = deque([root])
        while q:
            now = q.popleft()
            if data[index] != '#':
                now.left = TreeNode(int(data[index]))
                q.append(now.left)
            index += 1
            if data[index] != '#':
                now.right = TreeNode(int(data[index]))
                q.append(now.right)
            index += 1
        return root

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))