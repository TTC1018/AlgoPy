class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures)
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and temp > temperatures[stack[-1]]:
                popped = stack.pop()
                answer[popped] = idx - popped # 현재 인덱스까지 소요되는 날짜
            stack.append(idx) # 현재 인덱스 삽입
        return answer
