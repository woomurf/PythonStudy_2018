def solution(n):

    answer = 0

    primeList = [i for i in range(n+1)] # 리스트에 0 ~ n까지의 숫자를 집어넣는다.

    for i in primeList:
        if i != 0 and i != 1:
            for j in range(i*i,n+1,i): # i의 제곱부터 i의 배수를 제거한다.
                primeList[j] = 0

    primeList.remove(0) # 0과 1은 소수가 아니니 제거
    primeList.remove(1)

    for i in primeList: 
        if i != 0:
            answer += 1

    return answer
