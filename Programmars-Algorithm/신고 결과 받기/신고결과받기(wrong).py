def solution(id_list, report,k):
    report = list(set(report))
    report_sp = []
    report_sp.extend([report[i].split(" ") for i in range(len(report))])
    report_list = sum(report_sp, [])

    count = [[0] * len(id_list) for i in range(len(id_list))]
    answer = [0 for i in range(len(id_list))]

    for j in range(0,len(report_list),2):
        reporter = report_list[j]
        reported = report_list[j+1]
        count[id_list.index(reported)][id_list.index(reporter)]+=1

    for p in range(len(id_list)):
        if (sum(count[p]) >= k):
            for i, value in enumerate(count[p]):
                if value == 1:
                    answer[i] += 1

    return answer
    """
    for문이 너무 많이 사용돼서 오답 처리 된 것 같음
    몇몇 테스트 케이스에 대해 시간 초과됨... 
    for문을 최대한 줄여보자 -> dictionary형은 생각보다 처리 속도가 빠르다.
    for문을 줄일수도 있을 것 같고 이름 대신 index를 이용하면 저장하는 공간도 적게 사용할 것 같다.
    """