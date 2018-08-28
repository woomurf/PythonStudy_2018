def solution(s):
    answer = 0
    maxLength = 1

    for i in range(1,len(s)):
        length1 = 0
        length2 = 0

        if i < len(s)-1 and s[i-1] == s[i+1]:
            print("홀수 : ",i)
            comp = i-1
            now = i+1

            while s[comp] == s[now]:
                length1 += 2
                comp -= 1
                now += 1

                if comp < 0 or now >= len(s):
                    break
            length1 += 1
            print("length1 : ",length1)

        if s[i] == s[i-1]:
            print("짝수 : ",i)
            comp = i-1
            now = i

            while s[comp] == s[now]:
                length2 +=2
                comp -= 1
                now += 1

                if comp < 0 or now >= len(s):
                    break

        if length1 < length2 :
            length1 = length2

        if maxLength < length1 :
            maxLength = length1


    return maxLength


#문자열 str 이 str = "m" 이면 길이를 1로 본다.
