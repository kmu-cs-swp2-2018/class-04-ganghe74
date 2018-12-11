from observer.observable import Observable
import random

class Model(Observable):
    def __init__(self):
        super().__init__()
        self.__N = 4
        self.__field = [[0 for j in range(6)] for i in range(6)]
        self.__score = 0
        self.__tries = 0 # try는 파이썬 문법과 충돌

    @property
    def N(self):
        return self.__N

    @property
    def field(self):
        return self.__field

    @property
    def score(self):
        return self.__score

    @property
    def tries(self):
        return self.__tries

    @N.setter
    def N(self, N):
        self.__N = N
        self.notify()

    @field.setter
    def field(self, field):
        self.__field = field
        self.notify()

    @score.setter
    def score(self, score):
        self.__score = score
        self.notify()

    @tries.setter
    def tries(self, tries):
        self.__tries = tries
        self.notify()

    def generate(self, num): # 필드가 꽉차있을때 (0이없을때) generate하면 에러남
        row = random.randrange(self.N)
        column = random.randrange(self.N)
        if self.field[row][column] == 0:
            self.field[row][column] = num
        else:
            self.generate(num)
            return
        print("generate", num, "at", row, column)
        self.notify()

    def isMovable(self, direction): # 필드가 direction 방향으로 이동가능한가?
        dic = {"up":(-1,0), "down":(1,0), "left":(0,-1), "right":(0,1)}
        dy = dic[direction][0]
        dx = dic[direction][1]
        for row in range(self.N):
            for column in range(self.N):
                ny = row + dy
                nx = column + dx
                if 0 <= ny < self.N and 0 <= nx < self.N:
                    if self.field[row][column] != 0:
                        if self.field[row][column] == self.field[ny][nx] or self.field[ny][nx] == 0:
                            return True

        return False

    def isFinished(self): # 게임이 끝낫는가? ( 더 움직일수 없는가? )
        dy = [1,-1,0,0]
        dx = [0,0,1,-1]
        for row in range(self.N):
            for column in range(self.N):
                if self.field[row][column] == 0:
                    return False
                for k in range(4):
                    ny = row + dy[k]
                    nx = column + dx[k]
                    if 0 <= ny < self.N and 0 <= nx < self.N:
                        if self.field[row][column] == self.field[ny][nx]:
                            return False
        return True


if __name__ == '__main__': # 유닛테스트때 사용예정
    model = Model()
    print(model.field)
    print(model.isFinished())
    print("is movable with \"up\"?", model.isMovable("up"))
    print()

    model.field = [[2,2,2,2], [2,2,2,2], [2,2,2,2], [2,2,2,2]]
    print(model.field)
    print(model.isFinished())
    print("is movable wtih \"up\"?", model.isMovable("up"))
    print()

    model.field = [[2,4,2,4], [4,2,4,2], [2,4,2,4], [4,2,4,2]]
    print(model.field)
    print(model.isFinished())
    print("is movable with \"up\"?", model.isMovable("up"))
    print()
    
    model.field = [[2,4,2,4], [4,2,4,2], [2,4,2,4], [4,2,4,0]]
    print(model.field)
    print(model.isFinished())
    print("is movable with \"up\"?", model.isMovable("up"))
    print("is movable with \"down\"?", model.isMovable("down"))
    print("is movable with \"left\"?", model.isMovable("left"))
    print("is movable with \"right\"?", model.isMovable("right"))
    print()

    model.generate(123)
    print(model.field)
    print(model.field[0][0])
    model.field[0][0] = 1234
    print(model.field)
    print()

    model.field = [[2,0,0,0], [0,0,0,0], [0,0,0,0], [0,0,0,0]]
    print(model.field)
    print("is movable with \"up\"?", model.isMovable("up"))
    print("is movable with \"down\"?", model.isMovable("down"))
    print("is movable with \"left\"?", model.isMovable("left"))
    print("is movable with \"right\"?", model.isMovable("right"))