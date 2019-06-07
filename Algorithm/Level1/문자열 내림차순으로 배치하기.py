def solution(s):
    answer = []
    for i in range(len(s)):
        answer.append(s[i])

    answer.sort(reverse =True)

    string = ''

    for i in answer:
        string += i

    return string
