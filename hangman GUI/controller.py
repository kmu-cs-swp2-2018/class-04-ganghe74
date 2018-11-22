class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.view.guessButton.clicked.connect(self.guess)
        self.view.newGameButton.clicked.connect(self.newGame)

    # 추측을 1회 시행
    def guess(self):
        char = self.view.charInput.text()
        self.model.message = "아래에 메세지 입력후 Guess 클릭!"
        # 알파벳이 아니면 에러출력, return
        if char.isalpha()==False:
            self.model.message = "알파벳을 입력해 주세요."
            return
        # 1글자가 아니면 에러출력, return
        if len(char) != 1:
            self.model.message = "입력해 주세요."
            return
        # 이미 추측한 문자인 경우 에러출력, return
        if char in self.model.guessedChars:
            self.model.message = "You already guessed \"" + char + "\""
            return
        #대소문자 구별 하지 않기.
        if ord(char)<97:
            char=chr(ord(char)+32)

        self.model.addGuessedChar(char+" ")

        # 문자를 맞추면 model.currentStatus 의 공백을 채움
        # 못맞추면 numTries증가
        if char in self.model.secretWord:
            self.model.fillBlank(char)
            self.model.message="맞았습니다..기회 : "+str(6-self.model.numTries)
        else:
            self.model.incNumTries()
            self.model.message="틀렸습니다..기회 : "+str(6-self.model.numTries)
        #guess버튼을 누르면 입력창이 클리어 해짐
        self.view.charInput.clear()

        if self.model.isFinished():
            if self.model.isSuccess():
                self.model.message = "Success"
            if self.model.isFail():
                self.model.message = "GAME OVER 정답은 : "+self.model.secretWord+"입니다."

            self.view.guessButton.setDisabled(True)

    def newGame(self, char):
        self.model.secretWord = self.model.word.randFromDB()
        self.model.guessedChars = "사용 글자 : "
        self.model.currentStatus = "_" * len(self.model.secretWord)
        self.model.numTries = 0
        self.model.message = "아래에 입력하고 버튼을 누르세요."
        self.view.guessButton.setDisabled(False)

if __name__ == '__main__':
    import sys
    from model import Model
    from view import Layout
    from PyQt5.QtWidgets import QApplication
    app = QApplication(sys.argv)
    model = Model()
    view = Layout()
    controller = Controller(model, view)
    
    model.register(view.hangmanView, view.currentWordView, view.guessedCharsView, view.messageView)
    model.notify()

    view.show()
    sys.exit(app.exec_())