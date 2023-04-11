import sys

I=sys.stdin.readline

a=[int(I())for i in range(int(I()))]
d=[0,a[0],0]
for i in a[1:]:
    d=[max(d),d[0]+i,d[1]+i]  
print(max(d))
        
        
    
        