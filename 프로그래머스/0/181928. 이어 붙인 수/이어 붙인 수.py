def solution(num_list):
    a=[]
    b=[]
    for i in range(0,len(num_list)):
        if num_list[i]%2==0:
            a.append(str(num_list[i]))
        else:
          b.append(str(num_list[i]))
    answer= int(''.join(a))+int(''.join(b))
    return answer