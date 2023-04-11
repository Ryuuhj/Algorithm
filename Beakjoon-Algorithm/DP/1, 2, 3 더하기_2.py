cnt = int(input())

for j in range(cnt):
    num = int(input())
    way = [0]*(num+1)

    for i in range(1, num+1):
        if i == 1:
            way[i] = 1
        elif i == 2:
            way[i] = 2
        elif i == 3:
            way[i] = 4
        else:
            way[i] = way[i-1] + way[i-2] + way[i-3]
    
    print(way[num])
