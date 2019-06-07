def solution(s):
    lens = len(s)

    if lens%2 == 0:
        answer = s[(lens-1)//2] + s[(lens-1)//2 +1]
    else:
        answer = s[(lens-1)//2]

    return answer
