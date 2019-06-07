def solution(s, n):
    answer = ''

    for i in s:
        if i != ' ':
            if ord(i) < ord('a'):  # 대문자이면
                if ord(i) + n > ord('Z'): # Z 넘어가면
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i) + n)
            else: # 소문자
                if ord(i) + n > ord('z'): # z 넘어가면
                    answer += chr(ord(i) + n - 26)
                else:
                    answer += chr(ord(i)+n)
        else :
            answer += ' '


    return answer
