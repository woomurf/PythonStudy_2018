def solution(n):
    answer = []

    def hanoi(a,b,c,n):
        if n == 1:
            answer.append([a,c])
        else:
            hanoi(a,c,b,n-1)
            answer.append([a,c])
            hanoi(b,a,c,n-1)

    hanoi(1,2,3,n)

    return answer
