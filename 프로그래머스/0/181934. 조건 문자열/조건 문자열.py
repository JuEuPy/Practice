def solution(ineq, eq, n, m):
    a=0
    if ineq==">":
        a+=10
    if eq=="=":
        a+=1
    if a == 0 :
        return int(n<m)
    elif a == 1 :
        return int(n<=m)
    elif a == 10 :
        return int(n>m)
    else :
        return int(n>=m)