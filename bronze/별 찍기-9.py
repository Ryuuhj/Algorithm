cnt = int(input())
for i in range(1,cnt+1):
    print(' '*(i-1)+'*'*(2*(cnt-i)+1))
for j in range(2,cnt+1):
    print(' '*(cnt-j)+'*'*(2*j-1))