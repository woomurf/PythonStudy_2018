def solution(board):
    length = len(board)
    line_length = len(board[0])
    maxArea = 0

    if length < 2 or line_length < 2:
        for i in range(length):
            for j in range(line_length):
                if board[i][j] == 1:
                    maxArea = 1
                    break
    else:
        for i in range(1,length):
            for j in range(1,line_length):
                if board[i][j] == 1:
                    board[i][j] += min(board[i-1][j],board[i-1][j-1],board[i][j-1])

                if board[i][j] > maxArea:
                    maxArea = board[i][j]

    if maxArea == 0:
        for i in range(length):
            if board[i][0] == 1:
                maxArea = 1
                break

        for j in range(line_length):
            if board[0][j] == 1:
                maxArea = 1
                break

    return maxArea**2

"""
점화식을 이용한 방법이다. 한 좌표에서 3개의 좌표만 검사하기 때문에 효율적임.
"""
