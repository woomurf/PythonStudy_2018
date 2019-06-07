def solution(s):
    answer = ''

    list1 = s.split(' ')

    for index,string in enumerate(list1):
        list1[index] = string.title()
        
    answer  = (' ').join(list1)

    return answer
