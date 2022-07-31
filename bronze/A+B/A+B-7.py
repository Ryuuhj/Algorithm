import sys

for i in range(int(sys.stdin.readline())):
    number = list(map(int,sys.stdin.readline().split()))
    print("Case #%d:%d"%(i+1, number[0]+number[1]))
