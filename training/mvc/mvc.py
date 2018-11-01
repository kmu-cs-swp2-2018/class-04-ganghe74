import sys
from PyQt5.QtWidgets import QApplication
from view import MainView
from model import Model
from controller import Controller

class App(QApplication):
    def __init__(self, sys_argv, fileName):
        super(App, self).__init__(sys_argv)
        
        self.fileName = fileName
        self.model = Model()
        self.controller = Controller(self.model, self.fileName)
        self.view = MainView(self.model, self.controller)
        self.view.show()       

if __name__ == '__main__':    
    app = App(sys.argv, 'assignment6.dat')
    sys.exit(app.exec_())