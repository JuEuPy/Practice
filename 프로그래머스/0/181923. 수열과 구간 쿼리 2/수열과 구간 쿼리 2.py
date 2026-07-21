def solution(arr, queries):
    answer=[]
    for a,b,c in queries:
        temp=[]
        for i in range(a,b+1):
            if arr[i]>c:
               temp.append(arr[i])
        if len(temp)!=0:
            answer.append(min(temp))
        else:
            answer.append(-1)
            
    return answer