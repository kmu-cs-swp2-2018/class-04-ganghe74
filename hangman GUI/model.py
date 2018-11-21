from word import Word
from hangmanList import hangmanList
from observer.observable import Observable


class Model(Observable):
    def __init__(self):
        super().__init__()
        self.word = Word('words.txt')
        self.secretWord = self.word.randFromDB()
        self.__numTries = 0  # 7이되면 gameOver
        self.hangmanList = hangmanList
        self.__currentStatus = "_"*len(self.secretWord)
        self.__guessedChars = ""
        self.__message = ""

    @property
    def numTries(self):
        return self.__numTries

    @property
    def guessedChars(self):
        return self.__guessedChars

    @property
    def hamgmanList(self):
        return self.__hamgmanList

    @property
    def currentStatus(self):
        return self.__currentStatus

    @property
    def message(self):
        return self.__message

    @numTries.setter
    def numTries(self, num):
        self.__numTries = num
        self.notify()

    @currentStatus.setter
    def currentStatus(self, char):
        self.__currentStatus = char
        self.notify()
    
    @guessedChars.setter
    def guessedChars(self, char):
        self.__guessedChars = char
        self.notify()

    @message.setter
    def message(self, char):
        self.__message = char
        self.notify()

    def incNumTries(self):
        self.__numTries += 1
        self.notify()

    def addGuessedChar(self, char):
        self.__guessedChars += char

    def fillBlank(self, char):
        for i in range(len(self.secretWord)):
            if self.secretWord[i] == char:
                self.__currentStatus = self.__currentStatus[:i] + char + self.__currentStatus[i+1:]
        self.notify()

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