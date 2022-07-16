class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expand(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]: # 팰린드롬 조건 충족하는 동안은 인덱스를 계속 양쪽으로 확장
                left -= 1
                right += 1
            left += 1 # 멈추기 이전까지 팰린드롬이므로 다시 인덱스 더해줌
            return s[left:right]

        if len(s) < 2 or s == s[::-1]:
            return s

        max_pal = ''
        for i in range(len(s)):
            max_pal = max(max_pal, expand(i, i + 1),
                          expand(i, i + 2), key=len) # 홀수개, 짝수개 따로 계산한다

        return max_pal