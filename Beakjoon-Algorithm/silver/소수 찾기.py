length = int(input())
numList = list(map(int, input().split()))
cnt = 0

for num in numList:
  if num == 1:
    cnt+=1
    continue
  for i in range(2,num):
    if num%i==0:
      cnt +=1
      break

print(length-cnt)