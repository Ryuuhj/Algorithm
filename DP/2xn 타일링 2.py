num = int(input())
way = [0]*(num+1)

for i in range(1, num+1): #입력값이 1일때 index error를 방지하기 위해 for문 안에서 함께 처리
    if i == 1:
        way[i] = 1
    elif i == 2:
        way[i] = 3
    else:
        way[i] = way[i-1] + way[i-2]*2
print(way[num]%10007)
    