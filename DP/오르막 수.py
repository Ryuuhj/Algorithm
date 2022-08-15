import sys

num = int(sys.stdin.readline())
#오르막 수 담을 2차원 배열 dp[0~100][0~9] 생성 (입력 최대값 1000)
dp=[[0] * 10 for i in range(1001)]
#dp[0]=[0,0,0,0,0,0,0,0,0,0]로 두고, 길이 1인 경우 세팅
dp[1] = [1,1,1,1,1,1,1,1,1,1] #0으로 시작 가능하므로 모두 1

#dp[i][j] = ∑(k=0/j-1) dp[i-1][k]을 중첩 for문을 이용해 구현
for i in range(2,num+1):
    #0으로 끝나는 경우의 수는 항상 1 (0-0-...-0)
    dp[i][0] = 1
    for j in range (1,10):
        dp[i][j] = sum(dp[i-1][:j+1])

print(sum(dp[num])%10007)