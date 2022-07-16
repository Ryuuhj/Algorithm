people = [0]
for i in range(1,11):
  cnt =list(map(int,input().split()))
  people.append(people[2*(i-1)]-cnt[0])
  people.append(people[2*i-1]+cnt[1])
print(max(people))