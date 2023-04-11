height = [int(input()) for i in range(9)]
e1,e2 = 0,0

for i in range(9):
    for j in range(i+1,9):
        if sum(height) - (height[i] + height[j]) == 100:
            e1 = height[i]
            e2 = height[j]
height.remove(e1)
height.remove(e2)

print('\n'.join(map(str,sorted(height))))