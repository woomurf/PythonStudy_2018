def solution(phone_number):

    answer = ''
    length = len(phone_number)

    for i in range(length-4):
        answer += '*'

    for i in range(4,0,-1):
        answer += phone_number[-i]

    return answer
