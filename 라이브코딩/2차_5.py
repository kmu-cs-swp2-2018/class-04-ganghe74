def different(s1, s2):
    answer = 0
    s1 = s1.lower()
    s2 = s2.lower()
    for i in range(len(s1)):
        if s1[i] == s2[i]:
            answer += 1
    return answer

def solution(s, l):
    answer = []
    high = 0
    for x in l:
        diff = different(s, x)
        if diff > high:
            high = diff
            answer = [x]
        elif diff == high:
            answer.append(x)
    return answer