from fractions import gcd

def solution(arr):
    answer = 0

    for e in range(len(arr)-1):
        arr[e+1] =  arr[e]*arr[e+1]/gcd(arr[e],arr[e+1])

    answer = arr[-1]

    return answer
