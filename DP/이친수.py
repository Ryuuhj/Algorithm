import sys

num = int(sys.stdin.readline())

dp=[[0]*2 for i in range(91)]

for i in range(1,num+1):
    if i == 1 or i == 2:
        dp[i][0] = 1
        dp[i][1] = 0
    elif i == 3:
        dp[i][0]=2
        dp[i][1]=1
    else:
        dp[i][0] = dp[i-1][0]*2 - dp[i-1][1]
        dp[i][1] = dp[i-1][1] + dp[i-2][1]
        
print(dp[num][0])
        