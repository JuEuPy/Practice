def solution(code):
    mode = 0
    answer = []
    for i in range(0,len(code)):
        if code[i]=="1":
            mode = 1- mode
        elif i%2==mode:
            answer.append(code[i])
    return ''.join(answer) if ''.join(answer)!='' else "EMPTY"