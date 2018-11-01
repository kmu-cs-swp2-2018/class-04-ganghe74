class Guess:
    
    def __init__(self, word):
        self.secretWord = word 
        self.guessedChars = ""
        self.numTries = 0
        self.currentStatus = "_"*len(self.secretWord)
        self.foundChars = ""

    def display(self):
        print("Current: ", self.currentStatus)
        print("Tries: ", self.numTries)

    def guess(self, character):
        self.guessedChars += character
        if character in self.secretWord:
            self.foundChars += character
            self.currentStatus = ""
            for x in self.secretWord:
                if x in self.foundChars:
                    self.currentStatus += x
                else :
                    self.currentStatus += "_"
        else:
            self.numTries += 1

        if self.currentStatus == self.secretWord:
            return True
        return False