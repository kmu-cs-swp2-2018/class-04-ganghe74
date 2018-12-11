from model import Model

def up(lists, size) :
    score = 0
    for k in range(5) :
        for i in range(5) :
            for j in range(6) :
                n = lists[i][j]
                if n == 0 :
                    if lists[i+1][j] != 0 :
                        lists[i][j] = lists[i+1][j]
                        lists[i+1][j] = 0
    for i in range(5) :
        for j in range(6) :
            n = lists[i][j]
            if lists[i][j] == lists[i+1][j] :
                lists[i][j] = n*2
                lists[i+1][j] = 0
                score += n*2
    for i in range(2) :
        for i in range(5) :
            for j in range(6) :
                n = lists[i][j]
                if n == 0 :
                    if lists[i+1][j] != 0 :
                        lists[i][j] = lists[i+1][j]
                        lists[i+1][j] = 0
    return lists, score

def down(lists, size) :
    score = 0
    for k in range(5) :
        for i in range(size-1, 0, -1) :
            for j in range(6) :
                n = lists[i][j]
                if n == 0 :
                    if lists[i-1][j] != 0 :
                        lists[i][j] = lists[i-1][j]
                        lists[i-1][j] = 0
    for i in range(size-1, 0, -1) :
        for j in range(6) :
            n = lists[i][j]
            if n == 0 :
                continue
            if lists[i-1][j] == n :
                lists[i][j] += n
                lists[i-1][j] = 0
                score += n*2
    for k in range(2) :
        for i in range(size-1, 0, -1) :
            for j in range(6) :
                n = lists[i][j]
                if n == 0 :
                    if lists[i-1][j] != 0 :
                        lists[i][j] = lists[i-1][j]
                        lists[i-1][j] = 0
    return lists, score

def left(lists, size) :
    score = 0
    for k in range(5):
        for i in lists:
            for j in range(6):
                n = i[j]
                if n == 0:
                    continue
                else:
                    if j - 1 < 0:
                        continue
                    if i[j-1] == 0 :
                        i[j-1] += n
                        i[j] = 0
    for i in lists :
        for j in range(6) :
            n = i[j]
            if n == 0 :
                continue
            else :
                if n == i[j-1] :
                    i[j-1] += n
                    i[j] = 0
                    score += n*2
    for k in range(2) :
        for i in lists :
            for j in range(6) :
                n = i[j]
                if n == 0 :
                    continue
                else :
                    if j-1 < 0 :
                        continue
                    if i[j-1] == 0 :
                        i[j-1] += n
                        i[j] = 0
    return lists, score

def right(lists, size) :
    score = 0
    for k in range(size-1) :
        for i in lists :
            for j in range(size) :
                n = i[j]
                if j == size-1 :
                    continue
                if n == 0 :
                    continue
                if i[j+1] == 0 :
                    i[j+1] = n
                    i[j] = 0
    for i in lists :
        for j in range(size) :
            n = i[j]
            if j == size-1 :
                continue
            if n == 0 :
                continue
            if i[j+1] == n :
                i[j+1] += n
                i[j] = 0
                score += 2*n
    for k in range(2) :
        for i in lists :
            for j in range(size) :
                n = i[j]
                if j == size-1 :
                    continue
                if n == 0 :
                    continue
                if i[j+1] == 0 :
                    i[j+1] = n
                    i[j] = 0
    return lists, score


if __name__ == '__main__':
    model = Model()
    for i in range(10):
        model.generate(2)
    print("=====Before=====")
    for row in model.field:
        print(row)

    print("\n=====After=====")
    result = left(model.field)
    for row in result:
        print(row)