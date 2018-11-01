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
            temp = ""
            for i in range(len(self.secretWord)):
                if self.secretWord[i] == character:
                    temp += character
                else:
                    temp += self.currentStatus[i]
            self.currentStatus = temp
        else:
            self.numTries += 1
        if self.currentStatus == self.secretWord:
            return True
        return False