from collections import Counter

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        # 재귀를 통한 문제 풀이
        set_s = set(s)
        sorted_alpha = sorted(set_s) # 중복 제거된 사전 순 정렬 알파벳들
        for char in sorted_alpha:
            suffix = s[s.index(char):] # 자신 앞의 알파벳들은 제거한 문자열
            if set_s == set(suffix): # 필수적으로 필요한 알파벳들이 존재한다면
                return char + self.removeDuplicateLetters(suffix.replace(char, ''))
        return ''

        # 스택을 통한 문제 풀이
        counter = Counter(s)
        stack = []
        fixed = set()

        for char in s:
            counter[char] -= 1
            if char not in fixed:
                # stack에 든 알파벳이 현재 알파벳보다 사전 순으로 뒤고, 없애도 되는 경우면 (아직 뒤쪽에 더 있으면)
                while stack and char < stack[-1] and counter[stack[-1]] > 0:
                    fixed.remove(stack.pop()) # 자리 고정 취소
                stack.append(char)
                fixed.add(char)
        return ''.join(stack)