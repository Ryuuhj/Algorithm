arr = list(map(int, input().split()))
n1, n2 = arr[0], arr[1]

for i in range(min(n1,n2),0,-1): #최대공약수 구하기
  if n1%i == 0 and n2%i == 0:
    div = i #최대공약수 -> div에 저장
    break

print(div) #최대공약수 출력
print(div*(n1//div)*(n2//div)) #최소공배수 (= 최대공약수 * 각각 최대공약수로 나눈 몫)