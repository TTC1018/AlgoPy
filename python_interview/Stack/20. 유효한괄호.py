class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open = {'(', '{', '['}
        dict = {')': '(', '}': '{', ']': '['}
        for b in s:
            if b in open:
                stack.append(b)
            else:
                if not stack or dict[b] != stack[-1]:
                    return False
                else:
                    stack.pop()

        if stack:
            return False
        return True