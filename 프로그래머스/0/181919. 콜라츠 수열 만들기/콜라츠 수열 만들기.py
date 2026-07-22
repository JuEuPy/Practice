def solution(n):
    answer = [n]
    print(n)
    while n != 1:
        if n%2:
            n=3*n+1
        else:
            n/=2
        answer.append(int(n))
    return answer