def solution(arr1, arr2):
    answer = []

    for i in range(len(arr1)):
        list1 = []
        for s in range(len(arr2[0])):
            ele = 0
            for j in range(len(arr2)):
                ele += arr1[i][j]*arr2[j][s]
            #    print('pair i : {}, j : {}, s : {}'.format(i,j,s))

            list1.append(ele)
        answer.append(list1)


    return answer
