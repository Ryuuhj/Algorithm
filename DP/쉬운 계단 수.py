import sys

num = int(sys.stdin.readline())
#계단 수 담을 2차원 배열 dp[0~num][0~9] 생성
dp=[[0] * 10 for i in range(num+1)]
#dp[0]=[0,0,0,0,0,0,0,0,0,0]로 두고, 계단 길이 1인 경우 세팅
dp[1] = [0,1,1,1,1,1,1,1,1,1]

#나머지 길이인 경우 규칙 적용
for i in range(2, num+1):
    #0, 9 로 끝나는 경우 (예외 적용) - dp[i][j] = 0 + dp[i-1][j+1 or j-1]
    dp[i][0] = dp[i-1][1]
    dp[i][9] = dp[i-1][8]
    #나머지 일반적인 경우 규칙 적용
    for j in range(1,9):
        dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

#길이가 n일때 경우의 수를 sum으로 구하고, 1,000,000,000으로 나눈 나머지 출력
print(sum(dp[num])%10**9)