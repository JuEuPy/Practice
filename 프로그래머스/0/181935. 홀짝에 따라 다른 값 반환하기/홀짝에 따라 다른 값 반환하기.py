def solution(n):
    answer=0
    if n%2==1:
        for i in range(1,n+1,2):
            answer += i
    else :
        for j in range(0,n+1,2):
            answer += (j**2)
    return answer