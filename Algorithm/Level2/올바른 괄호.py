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


"""
bin() 을 사용하면 2진수로 변환된 문자열을 받을 수 있다.
str.count()를 사용하면 원하는 문자가 문자열 내에 몇개나 있는지 알 수 있다.
"""
