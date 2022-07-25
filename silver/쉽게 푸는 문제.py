a, b = map(int, input().split())
n = 1
while True:
    if 1/2*n*(n+1) < b and 1/2*(n+1)*(n+2) > b:
      n += 1
      break
    elif 1/2*n*(n+1) == b:
      break
    n += 1

numlist = sum([[i] * i for i in range(1,n+1)], [])
print(sum(numlist[a-1:b]))