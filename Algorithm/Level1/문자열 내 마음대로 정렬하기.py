def solution(string, n):

    def keysort(x):
        return x[n]
    answer = []


    string.sort(key = string[n])

    for j in range(len(string)):
        for i in range(len(string)):
            if i < len(string)-1:

                first = string[i]
                second = string[i+1]

                if first[n] == second[n]:

                    if second < first:

                        string[i] = second
                        string[i+1] = first


    return string
