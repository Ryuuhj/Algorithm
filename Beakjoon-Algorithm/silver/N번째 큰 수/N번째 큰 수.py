cnt = int(input())
N = 3
arr = [list(map(int,(input().split()))) for k in range(cnt)]
for i in range(len(arr)):
    arr[i].sort(reverse=True)
    print(arr[i][N-1])