def getOne(n):
    one = 0

    while n is not 1:
        one += n%2
        n //= 2

    one += n
    return one

def solution(n):
    answer = 0
    one_n = getOne(n)
    nextBig = n
    one_next = 0

    while True:
        nextBig += 1
        one_next = getOne(nextBig)

        if one_next == one_n:
            break

    return nextBig
