def solution(A,B):
    answer = 0

    A.sort()
    B.sort(reverse=True)

    for i in range(len(A)):
        minA = A[i]
        maxB = B[i]

        answer += minA*maxB

    return answer
