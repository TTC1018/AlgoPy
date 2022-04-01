INF = int(1e9)
N = int(input())

mats = list(map(int, input().split()))
for i in range(N - 1):
    r, c = map(int, input().split())
    mats.append(c)

dp = [[INF] * N for _ in range(N)]
for i in range(N):
    dp[i][i] = 0

for i in range(N):
    for j in range(N - i):
        k = j + i
        if j == k:
            continue
        
        for l in range(j, k):
            dp[j][k] = min(dp[j][k], dp[j][l] + dp[l + 1][k] 
                           + mats[j]*mats[l + 1]*mats[k + 1])
print(dp[0][-1])

# A = mats[0], mats[1]
# B = mats[1], mats[2]
# C = mats[2], mats[3]
# D = mats[3], mats[4] 

# AB = mats[0]*mats[1]*mats[2]
# BC = mats[1]*mats[2]*mats[3]
# CD = mats[2]*mats[3]*mats[4]

# ABC (dp[0][2]) = AB C or A BC
# => AB C = dp[0][1] + dp[2][2] + mats[0]*mats[2]*mats[3]
# => A BC = dp[0][0] + dp[1][2] + mats[0]*mats[1]*mats[3]

#BCD (dp[1][3]) = BC D or B CD
# => BC D = dp[1][2] + dp[3][3] + mats[1]*mats[3]*mats[4]
# => B CD = dp[1][1] + dp[2][3] + mats[1]*mats[2]*mats[4]

# ABCD = ABC D or AB CD or A BCD
# => ABC D = dp[0][2] + dp[3][3]
# => AB CD = dp[0][1] + dp[2][3]
# => A BCD = dp[0][0] + dp[1][3]