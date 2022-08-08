def factorial(k):
    total = 1
    for i in range(2,k+1):
        total *= i
    return total

result = [1] #인덱스 0 (=2*1타일이 0개인 경우)의 경우의 수는 무조건 1
num = int(input())
for i in range(1, (num//2)+1):
    v = factorial(num-i)//(factorial(i)*factorial(num-2*i))
    result.append(v)
print(sum(result)%10007)