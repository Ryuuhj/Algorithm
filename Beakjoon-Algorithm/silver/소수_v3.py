import math

def PrimeNum(num):
    arr = [True for i in range(num+1)]
    arr[0],arr[1] = False, False
    for i in range(2, int(math.sqrt(num))+1):
        if arr[i] == True:
            j=2
            while i*j <= num:
                arr[i*j]=False
                j+=1
                
    return arr
               
M = int(input())
N = int(input())

primeArray = PrimeNum(N)
pnum =[]
for i in range(M, N+1):
    if primeArray[i] == True:
        pnum.append(i)
    else:continue
        

try:
  print("%d\n%d"%(sum(pnum), pnum[0]))
except IndexError:
  print(-1)