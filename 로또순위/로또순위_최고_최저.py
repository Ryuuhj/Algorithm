def solution(lottos, win_nums):
    first = 0
    last = 0
    dk = 0
    for lotto in lottos:
        if(win_nums.count(lotto)):
            last = last + 1
        if(lotto == 0):dk +=1 
    first = last + dk
    
    rank={0:6,1:6,2:5,3:4,4:3,5:2,6:1}
    
    answer = [rank[first],rank[last]]
    return answer

#print(solution([44, 1, 0, 0, 31, 25],[31, 10, 45, 1, 6, 19]))