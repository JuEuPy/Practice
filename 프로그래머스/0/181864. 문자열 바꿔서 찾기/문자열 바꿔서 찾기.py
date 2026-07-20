def solution(myString, pat):
    myString=''.join("B" if i == "A" else "A" for i in myString)
    return int(myString.find(pat)/2+1)
