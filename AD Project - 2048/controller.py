import push

class Controller:
    def __init__(self, model, startView, mainView):
        self.model = model
        self.startView = startView
        self.mainView = mainView
        self.startView.threeButton.clicked.connect(self.gameStart)
        self.startView.fourButton.clicked.connect(self.gameStart)
        self.startView.fiveButton.clicked.connect(self.gameStart)
        self.startView.sixButton.clicked.connect(self.gameStart)
        self.mainView.newGameButton.clicked.connect(self.newGame)
        self.mainView.upButton.clicked.connect(self.push)
        self.mainView.downButton.clicked.connect(self.push)
        self.mainView.rightButton.clicked.connect(self.push)
        self.mainView.leftButton.clicked.connect(self.push)
        self.mainView.keyPressed.connect(self.push)

    def gameStart(self):
        sender = self.startView.sender()
        n = int(sender.text()[0])
        self.model.N = n
        self.model.generate(2)
        self.startView.hide()
        self.mainView.g1.setN(n)
        self.mainView.show()

    def newGame(self):
        self.mainView.hide()
        self.model.tries = 0
        self.model.score = 0
        self.model.field = [[0 for i in range(6)] for j in range(6)]
        self.startView.show()

    def push(self, e=0):
        keys = {87:'up', 83:'down', 65:'left', 68:'right'}
        functions = {'up':push.up, 'down':push.down, 'left':push.left, 'right':push.right}
        if e == 0:
            sender = self.mainView.sender()
            direction = sender.text()
        elif e in keys:
            direction = keys[e]
        else:
            return
        
        if self.model.isMovable(direction):
            print("move with ", direction)
            self.model.field, score = functions[direction](self.model.field, self.model.N)
            self.model.score += score
            self.model.generate(2)
            self.model.tries += 1

        if self.model.isFinished():
            self.gameOver()
            self.mainView.gameOver()

    def gameOver(self):
        print("Game Over!!!!!!!!!!!!")

if __name__ == '__main__':
    import sys
    from view import mainView, startView
    from PyQt5.QtWidgets import QApplication
    from model import Model
    app = QApplication(sys.argv)
    model = Model()
    main = mainView()
    start = startView()
    controller = Controller(model, start, main)
    model.register(main)
    start.show()
    sys.exit(app.exec_())