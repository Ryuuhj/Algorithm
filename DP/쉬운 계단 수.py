import sys

num = int(sys.stdin.readline())
dp=[[0] * 10 for i in range(num+1)]

dp[1] = [0,1,1,1,1,1,1,1,1,1]

for i in range(2, num+1):
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[num])%10**10)