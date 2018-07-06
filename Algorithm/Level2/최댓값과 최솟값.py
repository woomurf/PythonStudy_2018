def solution(s):
    string = s.split(' ')

    maxint = -9999999
    minint = 9999999
    
    for i in string:
        i = int(i)
        if i > maxint:
            maxint = i
        if i < minint:
            minint = i

    answer = str(minint)+ ' '+str(maxint)

    return answer
