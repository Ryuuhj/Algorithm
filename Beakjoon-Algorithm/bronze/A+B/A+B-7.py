import sys
#횟수(=숫자 1개)를 받아올 때는 input을 쓰는게 더 효율적이다
cnt = int(input())

for i in range(cnt):
    a, b = map(int, sys.stdin.readline().split())
    print("Case #%d:"%(i+1),a+b) #a +b는 굳이 %d로 포맷팅 해줄 필요가 없어보인다.
