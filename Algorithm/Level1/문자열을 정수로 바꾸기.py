def solution(s):

    answer = 0
    string = ""

    if s[0] == '-':
        for i in range(len(s)):
            if i != 0:
                string += s[i]

        answer = 0 - int(string)
    else:
        answer = int(s)

    return answer
