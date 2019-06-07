def solution(n, m):
    answer = []

    max = m
    min = n

    if n > m :
        max = n
        min = m

    for i in range(min,0,-1):
        if max%i == 0 and min%i == 0:
            answer.append(i)
            answer.append(max*min/i)
            break


    return answer

"""
유클리드 호제법
max,min
while min is not 0:
    (max,min) = (min, max%min)

"""
