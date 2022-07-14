num = input()
nList = list(map(int, input().split()))
min = max = nList[0]
for k in nList:
  if k <= min:
    min = k
  elif k > max:
    max = k

print(min, max)