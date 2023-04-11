cnt = int(input())
N = 3
for i in range(cnt):
    num = list(map(int,input().split()))
    num.sort(reverse=True)
    print(num[N-1])
    