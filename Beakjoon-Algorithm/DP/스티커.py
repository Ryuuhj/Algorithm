cnt = int(input())

for i in range(cnt):
    num = int(input())
    #스티커 점수 입력값 저장 + 최대값 위한 중간값 갱신
    sticker = []
    for k in range(2):
        sticker.append(list(map(int, input().split())))
    #2열부터 최대값 비교해서 갱신
    for j in range(1, num):
        if j == 1:
        #1열 값 세팅 (런타임에러 방지)
            sticker[1][j] += sticker[0][j-1]
            sticker[0][j] += sticker[1][j-1]
        else:
            sticker[0][j] += max(sticker[1][j-1], sticker[1][j-2])
            sticker[1][j] += max(sticker[0][j-1], sticker[0][j-2])
    print(max(sticker[0][num-1], sticker[1][num-1]))
    
        