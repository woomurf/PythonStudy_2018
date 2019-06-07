def solution(seoul):

    n = 0

    for i in range(len(seoul)):
        if seoul[i] == "Kim":
            n = i

    where = str(n)

    answer = "김서방은 " + where +"에 있다"

    return answer
