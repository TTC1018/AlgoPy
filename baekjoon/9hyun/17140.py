import sys

r, c, k = map(int, input().split())
A = [list(map(int, input().split())) for _ in range(3)]

r, c = r - 1, c - 1
for sec in range(100):
    if A[r][c] == k:
        print(sec)
        sys.exit()
    
    

print(-1)