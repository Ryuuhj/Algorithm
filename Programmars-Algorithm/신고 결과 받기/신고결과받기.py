def solution(id_list, report,k):
    nidx={}
    answer=[]
    total=[]
    banID=[]
    report = list(set(report)) #집합은 순서가 없어 인덱스를 이용해서 값을 참조할 수 없다.. 따라서 list형으로 다시 전환해줬다.
    for i in range(0,len(id_list)):
        nidx[id_list[i]]= i #{'이름':대응하는 인덱스 번호} ;; 이게 더 찾기 편할듯
        answer.append(0) #[0,0,0 ... ] 생성
        total.append([]) #2차원 리스트 미리 정의- [[],[],[],[]]
    for l in report:
        report_sp = l.split()
        idx1 = nidx[report_sp[0]]
        idx2 = nidx[report_sp[1]]
        total[idx2].append(idx1)
        if (len(total[idx2])>=k):
            if idx2 not in banID: #이걸 추가 안해줘서 오류났었음
                banID.append(idx2)
    for i in banID:
        for index in total[i]:
            answer[index] +=1

    return answer