def solution(l, r):
    answer=[]
    n=0
    i=1
    while True:
        n=int(str(bin(i))[2:])*5
        if r >= n >= l:
            answer.append(n)
        elif n>r:
            break
        i+=1
    if len(answer) == 0:
        answer = [-1]
    return answer