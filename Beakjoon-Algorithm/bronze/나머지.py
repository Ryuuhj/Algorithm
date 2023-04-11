import sys

num = list(sys.stdin.readline().strip().replace(" ",""))
n = list(map(int,num))
a = (n[0]+n[1])%n[2]
b = (n[0]*n[1])%n[2]
print(a)
print(a)
print(b)
print(b)