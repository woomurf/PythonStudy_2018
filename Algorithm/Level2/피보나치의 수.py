def solution(n):
    answer = 0
    fibo = [0,1,1]

    for i in range(3,n+1):
        fibo.append(fibo[i-1]+fibo[i-2])

    answer = fibo[-1]%1234567

    return answer

    """
    def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
    """
