import sys

sum = 0
numlist = sys.stdin.readlines()
for c in numlist[1].rstrip():
    sum += int(c)

print(sum)
