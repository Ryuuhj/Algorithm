def solution(a, b):
    day = {0:"THU", 1:"FRI", 2:"SAT",3:"SUN",4:"MON",5:"TUE",6:"WED"}
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    total=b
    for m in range(1,a):
        total+=month[m-1]
    return day[total%7]