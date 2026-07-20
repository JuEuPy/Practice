def solution(rny_string):
    answer=[]
    for i in range(len(rny_string)):
        answer += "rn" if rny_string[i]=="m" else rny_string[i]
    return ''.join(answer)