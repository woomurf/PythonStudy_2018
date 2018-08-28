def solution(n):
    a,b = 0,1
    for i in range(n):
        a,b = b,a+b

    answer = b
    return answer%1000000007


#피보나치를 이용한 문제
