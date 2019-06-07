def solution(n):
    answer = 0

    for i in range(1,n+1):
        
        sum = 0
        j = i

        while sum < n:
            sum += j
            j += 1

        print('sum : ',sum)

        if sum == n:
            answer += 1

    return answer
