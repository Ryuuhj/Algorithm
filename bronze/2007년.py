month = [31,28,31,30,31,30,31,31,30,31,30,31]
day = ["SUN","MON","TUE","WED","THU","FRI","SAT"]
m, d = map(int, input().split())
print(day[((sum(i for i in range(m))+d)%7)])