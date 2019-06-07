def solution(s):

    answer = True

    if len(s) == 4 or len(s) == 6:
        for i in s:
            if i >= '0' and i <= '9':
    #            print("true {}".format(i))
            else:
    #            print("false {}".format(i))
                answer = False
    else:
        print(' 길이')
        answer = False

    return answer
