cnt = int(input())

w = [0]*10000
for i in range(cnt):
    w[i]=int(input())

dp= [0]*10000
dp[0]=w[0]
dp[1]=w[0]+w[1]
dp[2]=max(dp[1],max(w[0],w[1])+w[2])
for i in range(3,cnt):
    dp[i]=max(dp[i-2]+w[i], dp[i-3]+w[i-1]+w[i], dp[i-1])
print(max(dp))
        
        
    
        