cnt = int(input())
for i in range(1, cnt*2):
    if i <=cnt:
        print('*'*(i)+' '*(2*(cnt-i))+'*'*(i))
    else:
        print('*'*(2*cnt-i)+' '*(2*(i-cnt))+'*'*(2*cnt-i))