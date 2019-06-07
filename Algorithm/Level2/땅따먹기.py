def solution(land):
    answer = 0

    length = len(land)

    for i in range(length-1):
        land[i+1][0] += max(land[i][1],land[i][2],land[i][3])       # 가장 큰 경우의 수를 저장한다.
        land[i+1][1] += max(land[i][0],land[i][2],land[i][3])
        land[i+1][2] += max(land[i][0],land[i][1],land[i][3])
        land[i+1][3] += max(land[i][0],land[i][1],land[i][2])

    answer = max(land[length-1][0],land[length-1][1],land[length-1][2],land[length-1][3])

    return answer



"""
 max(board[i][:j] + board[i][j + 1:])   # :j    j까지  j+1: j+1부터  검사 -> j는 빼고 검사한다.
"""
