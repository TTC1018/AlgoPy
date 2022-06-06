import sys
input = sys.stdin.readline


for _ in range(int(input())):
    N, M = map(int, input().split())
    visited = [False] * (N + 1)
    stu = [tuple(map(int, input().split())) for _ in range(M)]
    stu.sort(key=lambda x:(x[1], x[0])) # 한계치 낮은 순으로 정렬
    
    
    answer = 0
    for a, b in stu:
        for i in range(a, b + 1):
            if not visited[i]:
                visited[i] = True
                answer += 1
                break
    print(answer)