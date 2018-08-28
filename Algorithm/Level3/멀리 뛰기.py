def solution(n):

    if n == 1:
        return 1
    elif n == 2:
        return 2

    fn1 = 1
    fn2 = 2

    for i in range(n-2):
        fn1,fn2 = fn2,(fn1+fn2)

    return fn2%1234567
