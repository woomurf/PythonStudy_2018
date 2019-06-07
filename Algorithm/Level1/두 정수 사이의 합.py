def solution(a, b):

    if a > b :

        tmp = a
        a = b
        b = tmp

    sum = 0

    for i in range(b-a+1):
        sum += i+a

    return sum
