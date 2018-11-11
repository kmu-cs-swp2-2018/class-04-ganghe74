from word import Word
from hangmanList import hangmanList

class Model:
    def __init__(self):
        self.word = Word('words.txt')
        self.secretWord = self.word.randFromDB()
        self.numTries = 0 # 7이되면 gameOver
        self.hangmanList = hangmanList
        self.currentStatus = "_"*len(self.secretWord)
        self.guessedChars = ""

    def incNumTries(self):
        self.numTries += 1

    def addGuessedChar(self, char):
        self.guessedChars += char

    def fillBlank(self, char):
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == char:
                self.currentStatus = self.currentStatus[:i] + char + self.currentStatus[i+1:]

    def isSuccess(self):
        if self.secretWord == self.currentStatus:
            return True
        return False

    def isFail(self):
        if self.numTries >= 6:
            return True
        return False

    def isFinished(self):
        return self.isSuccess() or self.isFail()