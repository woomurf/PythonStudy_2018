def solution(n):
    answer = []
    country124 = [1,2,4]
    temp = 0 # 나머지
    quo = 0 # 몫
    sum124 = 0

    if n > 3 :
        while True:
            quo = n//3
            temp = n%3
            print('quo : {} , temp : {}'.format(quo, temp))

            if temp == 0:
                quo -= 1
                temp += 3

            answer.append(country124[temp-1])

            if quo <= 3:
                break

            n = quo

        answer.append(country124[quo-1])

    else :
        answer.append(country124[n-1])

    for i in range(len(answer)):
        ten = 1
        if i == 0:
            sum124 += answer[i]
        else :
            for j in range(i):
                ten*= 10
            sum124 += ten*answer[i]
        print ('sum124 : {}'.format(sum124))

    return str(sum124)


    """
    다른 사람의 풀이 중 인상적인 코드

    def change124(n):
    num = ['1','2','4']
    answer = ""


    while n > 0:
        n -= 1
        answer = num[n % 3] + answer  # string 이기 때문에 그냥 앞으로 온다...
        n //= 3

    return answer

    """
