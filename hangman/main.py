from model import Model
from view import View
from controller import Controller

model = Model()
view = View(model)
controller = Controller(model, view)

while not model.isFinished():
    view.printHangman()
    char = view.inputChar()
    controller.guess(char)

if model.isSuccess():
    view.printSuccess()
elif model.isFail():
    view.printFail()
else:
    view.printError("Game Finished with unknown error")