def PrimeNum(num):
    if num == 0 or num == 1:
        return False
    
    arr = [1 for i in range(num+1)]
    arr[0], arr[1], arr[-1] = 0, 0, 0
    
    for i in range(2, num+1):
        if arr[i] == 1:
            j = 2
            while i*j <= num:
                arr[i*j] = 0
                j += 1
                   
    for k in range(len(arr)):
        if arr[k] == 1:
            if num % k == 0:    
                return False
        else:
            continue
    return True
               
M = int(input())
N = int(input())

pnum = [i for i in range(M,N+1) if PrimeNum(i)]

try:
  print("%d\n%d"%(sum(pnum), pnum[0]))
except IndexError:
  print(-1)