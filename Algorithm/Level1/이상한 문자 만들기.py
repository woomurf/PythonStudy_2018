def solution(s):
    answer = ''
    List  = s.split(' ')
    print(List)

    for idx,j in enumerate(List):
        for index, i in enumerate(j):
            if index%2 != 0:
                answer += i.lower()
            else:
                answer += i.upper()

        if idx != len(List)-1:
            answer += ' '

    return answer
