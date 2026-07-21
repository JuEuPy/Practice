def solution(a, b, c):
    answer=a+b+c
    if len({a,b,c})==3:
        return answer
    answer*=(a**2+b**2+c**2)
    if len({a,b,c})==2:
        return answer
    answer *= (a**3+b**3+c**3)
    return answer