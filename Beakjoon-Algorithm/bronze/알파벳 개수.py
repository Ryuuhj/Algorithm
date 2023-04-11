import sys
s = list(sys.stdin.readline().strip())
count = []
a = 'abcdefghijklmnopqrstuvwxyz'
for c in range(26):
    count.append(s.count(a[c]))

print(*count)