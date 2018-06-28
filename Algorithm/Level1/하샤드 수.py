def solution(x):

    answer = True
    hashade = 0
    num = x

    while(x >= 10):
        hashade += x%10
        x //= 10

    hashade += x

    if num%hashade != 0:
        answer = False

    return answer
