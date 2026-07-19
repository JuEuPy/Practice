def solution(n, control):
  key=["w","s","d","a",1,-1,10,-10]
  for i in control:
    for j in range(4):
      if i==key[j]:
        n+=key[j+4]
  return n