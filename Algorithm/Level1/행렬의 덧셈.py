def solution(arr1, arr2):
    answer = [[]]
    rowlen = len(arr1)
    collen = len(arr1[0])
    """
    answer = arr1 으로 하면 answer을 arr1과 크기를 동일하게 만들 수 있다.

    """

    for i in range(rowlen):
        answer.append([])
        for j in range(collen):
            answer[i].append(arr1[i][j] + arr2[i][j]) # arr1[i].append(arr1[i][j] + arr2[i][j]) 로 하면 더욱 간단하게 해결 가능
    return answer[:-1]
