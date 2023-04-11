mincal = [0,0]
num = int(input())


for i in range(2,num+1):
    mincal.append(mincal[i-1]+1)
    if i%3 == 0:
         mincal[i] = min(mincal[i], mincal[i//3]+1)
    if i%2==0:
         mincal[i] = min(mincal[i], mincal[i//2]+1)
print(mincal[num])