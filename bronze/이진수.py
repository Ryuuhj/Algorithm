cnt=int(input())2
for i in range(cnt): 
  num = int(input())
  idx = 0
  bin=[]
  while True:
   if num%2 == 1:  
      bin.append(idx)
   num = num//2
   idx +=1
   if num is not 0: continue
   break
  print(*bin)