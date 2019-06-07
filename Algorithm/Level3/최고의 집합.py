def solution(n, s):
    answer = []
    if n > s:
        return [-1]

    avg = s//n
    temp = s%n

    for i in range(n):
        answer.append(avg)

    for i in range(temp):
        answer[i] += 1

    answer.sort()

    return answer

# 같은 수를 리스트에 넣어도 정답이다.
