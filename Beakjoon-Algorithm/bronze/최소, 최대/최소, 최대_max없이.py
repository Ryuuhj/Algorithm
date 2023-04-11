people = [0]
max = 0 
for i in range(1,11):
    
    cnt =list(map(int,input().split()))
    people.append(people[2*(i-1)]-cnt[0])
    people.append(people[2*i-1]+cnt[1])
    if people[-1] >= max:
        max = people[-1]
    elif people[-2] >= max:
        max = people[-2]

print(max)