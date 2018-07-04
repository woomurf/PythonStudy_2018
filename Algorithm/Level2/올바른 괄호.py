def solution(s):
    answer = False
    open_close = 0

    for bracket in s:
        if bracket == '(':
            open_close += 1
        else:
            open_close -= 1

        if open_close < 0:
            return False

    if open_close == 0:
        answer = True

    return answer
