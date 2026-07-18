def solution(a, b):
    a1 = str(a)+str(b)
    a2 = str(b)+str(a)    
    if a1 > a2:
      return int(a1)
    else :
      return int(a2)

    