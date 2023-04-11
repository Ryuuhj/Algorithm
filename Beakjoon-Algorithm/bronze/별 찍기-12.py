cnt = int(input())
for i in range(1, cnt+1):
    print(' '*(cnt-i)+'*'*(i))
for j in range(1, cnt):
    print(' '*(j)+'*'*(cnt-j))