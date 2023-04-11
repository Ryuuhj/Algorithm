def PrimeNum(num):
  for k in range(2, num):
    if num % k == 0:
      return False
  return True

M = int(input())
N = int(input())

pnum = [i for i in range(M,N+1) if PrimeNum(i)]

try:
  print("%d\n%d"%(sum(pnum), pnum[0]))
except IndexError:
  print(-1)