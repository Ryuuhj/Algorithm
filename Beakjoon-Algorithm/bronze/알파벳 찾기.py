import sys
s = list(sys.stdin.readline().strip())
count = [-1]*26
a = 'abcdefghijklmnopqrstuvwxyz'
for i in range(26):
    if a[i] in s:
        count[i] = s.index(a[i])

print(*count)