import sys
from view import mainView, startView
from PyQt5.QtWidgets import QApplication
from model import Model
from controller import Controller
from push import *

app = QApplication(sys.argv)
model = Model()
main = mainView()
start = startView()
controller = Controller(model, start, main)
model.register(main)
start.show()
sys.exit(app.exec_())