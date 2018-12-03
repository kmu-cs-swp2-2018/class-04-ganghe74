def invert_dict(d):
    inv = [(x, []) for x in set(d.values())]
    for alphabet in d:
        val = [x for x, y in inv].index(d[alphabet])
        if alphabet in d:
            inv[val][1].append(alphabet)
        else:
            continue

    return inv

def solution(string):
    d = {}
    for c in string:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    return str(invert_dict(d))