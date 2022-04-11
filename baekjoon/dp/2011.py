code = input()
dp = [0] * (len(code) + 1)
dp[0] = 1
c_len = len(code)

if code[0] == '0':
    print(0)
else:
    code = '0' + code
    
    # 1. 이전 경우의 수에 1~9 중 하나가 더해지는 것 체크
    # 한 자릿수 적은 경우의 수들에 수 한자리 수 하나 갖다 붙인 것이기 때문에
    # 이전 경우의 수 그대로 더해줌
    # 2. 직전의 수와 새로운 수가 10~26 중 하나의 수를 이루는 지 체크
    # 두 자릿수 적은 경우의 수들에 두자리 수 하나 갖다 붙인 것이기 때문에
    # 이전 경우의 수 그대로 더하기
    for i in range(1, c_len + 1):
        if 1 <= int(code[i]) <= 9:
            dp[i] += dp[i - 1]
        if 10 <= int(code[i - 1]) * 10 + int(code[i]) <= 26:
            dp[i] += dp[i - 2]
        dp[i] %= 1000000
    print(dp[c_len])