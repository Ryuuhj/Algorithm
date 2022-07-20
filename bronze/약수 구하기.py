l =list(map(int,input().split()))
num = l[0]
divisor=[]
try:
    for i in range(1,num+1):
        if num % i == 0:
          divisor.append(i)
    print(divisor[l[1]-1])
except IndexError:
  print(0)