def solution(n):
    answer = 0
    digit = 0
    List = []

    while( n >= 10):
        digit += 1
        List.append(n%10)
        n //= 10

    List.append(n)
    List.sort(reverse=True)

    for i in List:
        for j in range(digit):
            i = i*10
        digit -= 1
        answer += i

    return answer
