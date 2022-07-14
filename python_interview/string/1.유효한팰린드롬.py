import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        # 정규식을 이용한 교재 풀이
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s) # [] 안에서는 ^ = not
        return s == s[::-1]

        # 투 포인터 풀이
#         new_s = ''.join([string.lower() for string in s if string.isalnum()])

#         left, right = 0, len(new_s) - 1
#         while left < right:
#             if new_s[left] != new_s[right]:
#                 return False
#             left += 1
#             right -= 1
#         return True
