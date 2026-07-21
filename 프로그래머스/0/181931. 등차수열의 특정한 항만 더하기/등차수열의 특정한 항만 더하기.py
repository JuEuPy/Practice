def solution(a, d, included):
    answer = 0
    for i in range(0,len(included)):
        n=a+d*i
        if included[i]:
            answer+=n
    return answer