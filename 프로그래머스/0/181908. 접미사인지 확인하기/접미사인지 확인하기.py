def solution(my_string, is_suffix):
    a=my_string.find(is_suffix,len(my_string)-len(is_suffix))
    if a==-1:
      return 0
    else:
      return 1