import copy

def solution(arr):

    answer=[]

    min = copy.deepcopy(arr)
    min.sort()
    arr.remove(min[0])

    if len(arr) == 0:
        arr.append(-1)
    return arr
