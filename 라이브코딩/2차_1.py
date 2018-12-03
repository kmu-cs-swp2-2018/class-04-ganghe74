def solution(L, t):
    answer = []
    for x in L:
        if x >= t:
            answer.append(x)
    return answer