def solution(s):
    answer = False
    pstack = 0
    ystack = 0

    for stack in s:
        if stack == 'p' or stack == 'P':
            pstack += 1
        elif stack == 'y' or stack =='Y':
            ystack += 1

    if pstack == ystack:
        answer = True
    else:
        answer = False

    return answer
