import math

def solution(n):

    answer = 0
    sqr = math.sqrt(n)
    sqr *= 10

    if sqr%10 == 0:
        sqr //= 10
        answer = int(sqr) +1
        answer *= answer
    else :
        answer = -1

    return answer
