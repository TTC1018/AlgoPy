import sys
input = sys.stdin.readline


N, K = int(input()), int(input())
sensor = list(map(int, input().split()))
sensor.sort()

dist = [sensor[i + 1] - sensor[i] for i in range(N - 1)] # 센서 간의 거리
dist.sort()
print(sum(dist[:N - K])) # K개의 수신기로 N - K 개의 센서간의 거리를 커버함