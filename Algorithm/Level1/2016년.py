def solution(a, b):

    day = ['THU','FRI','SAT','SUN','MON','TUE','WED']

    date = 0

    for i in range(a):
        if i == 2:
            date += 29
        elif i == 1 or i == 3 or i == 5 or i == 7 or    i==  8 or i == 10 or i == 12:
            date += 31
        elif i == 4 or i == 6 or i == 9 or i == 11:
            date += 30

    date += b
    date %= 7

    answer = day[date]
    return answer
