from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLayout, QGridLayout
from PyQt5.QtWidgets import QHBoxLayout, QVBoxLayout
from PyQt5.QtWidgets import QTextEdit, QLineEdit, QPushButton, QToolButton, QSizePolicy, QLabel

class GridLayout(QGridLayout):
    def __init__(self):
        super().__init__()
        
        self.labels = [[QLabel("0") for i in range(6)] for i in range(6)]
        for row in self.labels:
            for lb in row:
                lb.setStyleSheet(
                    "font-size : {0:0.0f}px;"
                    "background-color : hsl({1:0.0f}, 100%, 50%);"
                    "min-width: 120px;"
                    "min-height: 120px;"
                    .format(10, 20)
                )
        for i in range(6):
            for j in range(6):
                self.addWidget(self.labels[i][j], i, j)

    def setN(self):
        b = self.sender()
        n = int(b.text())
        for i in range(6):
            for j in range(6):
                self.labels[i][j].setVisible(False)
        for i in range(n):
            for j in range(n):
                self.labels[i][j].setVisible(True)

        

class View(QWidget) :
    def __init__(self, parent=None):
        super().__init__(parent)

        self.g1 = GridLayout()

        self.button3 = QPushButton("3")
        self.button4 = QPushButton("4")

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.button3)
        self.hbox1.addWidget(self.button4)

        self.vbox1 = QVBoxLayout()
        self.vbox1.addLayout(self.hbox1)
        self.vbox1.addLayout(self.g1)

        self.setLayout(self.vbox1)

        self.button3.clicked.connect(self.g1.setN)
        self.button4.clicked.connect(self.g1.setN)

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    view = View()
    view.show()
    sys.exit(app.exec_())