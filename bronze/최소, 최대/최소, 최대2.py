import sys

cnt = int(input())
nlist = list(map(int, sys.stdin.readline()))

print("%d %d"%(min(nlist),max(nlist)))
