class View:
    def __init__(self, model):
        self.model = model
        
    def inputChar(self):
        return input("Select a letter: ")

    def printHangman(self):
        print(self.model.hangmanList[6-self.model.numTries])
        print("Current:", self.model.currentStatus)
        print("Tries:", self.model.numTries)

    def printSuccess(self):
        print("\nword ["+self.model.secretWord+"]")
        print("Success")

    def printFail(self):
        print("\nword ["+self.model.secretWord+"]")
        print("guess ["+self.model.currentStatus+"]")
        print("Fail")

    def printError(self, msg):
        print(msg)