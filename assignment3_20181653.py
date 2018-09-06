import pickle
dbfilename = 'assignment3.dat'
def readScoreDB():
    try:
        fH = open(dbfilename, 'rb')
    except FileNotFoundError as e:
        print("New DB: ", dbfilename)
        return []
    else:
        print("Open DB: ", dbfilename)
    scdb = pickle.load(fH)
    fH.close()
    return scdb

def writeScoreDB(scdb):
    fH = open(dbfilename, 'wb')
    pickle.dump(scdb, fH)
    fH.close()

def doScoreDB(scdb):
    while(True):
        inputstr = input("Score DB > ")
        if inputstr == "": continue
        parse = inputstr.split(" ")
        if parse[0] == 'add':
            try:
                parse[2] = int(parse[2])
                parse[3] = int(parse[3])
            except ValueError as e:
                print("Age and Score must be integer")
                continue
            except IndexError as e:
                print("Age or Score not given")
            else:
                record = {'Name':parse[1], 'Age':parse[2], 'Score':parse[3]}
                scdb += [record]
        elif parse[0] == 'del':
            if len(parse) == 1:
                print("Name not given")
                continue
            for p in scdb:
                if p['Name'] == parse[1]:
                    scdb.remove(p)
                    break
        elif parse[0] == 'show':
            sortKey = 'Name' if len(parse) == 1 else parse[1]
            if not (sortKey == 'Name' or sortKey == 'Age' or sortKey == 'Score'):
                print("Invalid Key Value:", sortKey)
                continue
            showScoreDB(scdb, sortKey)
        elif parse[0] == 'quit':
            break
        elif parse[0] == 'find':
            if len(parse) == 1:
                print("Name not given")
                continue
            for p in scdb:
                if p['Name'] == parse[1]:
                    for attr in sorted(p):
                        print(attr, "=", p[attr], end=' ')
                    print()
                    break
                else:
                    continue
        elif parse[0] == 'inc':
            if len(parse) == 1:
                print("Name not given")
                continue
            try:
                amount = int(parse[2])
            except ValueError as e:
                print("Score must be integer")
            except IndexError as e:
                print("Score not given")
            else:
                for i in range(len(scdb)):
                    if scdb[i]['Name'] == parse[1]:
                        scdb[i]['Score'] += amount
                        break
        elif parse[0] == 'del':
            for i in range(len(scdb)):
                if scdb[i]['Name'] == parse[1]:
                    del scdb[i]
        else:
            print("Invalid command: " + parse[0])

def showScoreDB(scdb, keyname):
    for p in sorted(scdb, key=lambda person: person[keyname]):
        for attr in sorted(p):
            print(attr, "=", p[attr], end=' ')
        print()


scoredb = readScoreDB()
doScoreDB(scoredb)
writeScoreDB(scoredb)
