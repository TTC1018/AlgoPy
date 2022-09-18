class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        passed = {}
        answer = 0
        start = 0

        for idx, char in enumerate(s):
            # 이미 확인한 알파벳,
            if char in passed and start <= passed[char]:
                start = passed[char] + 1
            # 중복 없음
            else:
                answer = max(answer, idx - start + 1) # 최대 길이 갱신

            # 지나간 알파벳의 위치 기록하기
            passed[char] = idx

        return answer