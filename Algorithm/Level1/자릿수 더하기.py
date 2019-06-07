def solution(n):

    answer = 0
    last = 0
    
    while( n >= 10):
        last = n%10
        answer += last
        n //= 10

    answer += n


    return answer
