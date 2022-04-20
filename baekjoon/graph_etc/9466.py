import sys
input = sys.stdin.readline


def find_team(node):
    team = [node]
    while True:
        node = s[node] # 부모
        if not visited[node]:
            visited[node] = True
            team.append(node)
        else: # 탐색 중단 (싸이클 생성 or 이미 전에 낙오된 곳)
            if node in team: #싸이클인 지점
                return team.index(node)
                # 완전한 싸이클 형태면 제외 인원 없음 (0 리턴)
                # 중간에 끊고 싸이클 생기는 형태면 싸이클 밑으로 제거
            else: # 이미 전에 싸이클 안 된다고 판단한 곳
                return len(team) # 모두 낙오


for _ in range(int(input())):
    n = int(input())
    s = [0] + list(map(int, input().split()))
    visited = [False] * (n + 1)

    answer = 0
    for i in range(1, n + 1):
        if not visited[i]:
            visited[i] = True
            answer += find_team(i)
    print(answer)