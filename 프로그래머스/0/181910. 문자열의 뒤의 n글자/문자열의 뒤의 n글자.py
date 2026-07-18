def solution(my_string, n):
  answer=[]
  for i in range(0,len(my_string)):
    if i>len(my_string)-n-1:
      answer += my_string[i]
  return ''.join(answer)