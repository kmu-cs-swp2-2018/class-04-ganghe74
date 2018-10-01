import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()
        self.dbfilename = 'assignment6.dat'
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()

    def initUI(self):
        hbox1 = QHBoxLayout()
        nameLabel = QLabel('Name:')
        nameLine = QLineEdit('')
        ageLabel = QLabel('Age:')
        ageLine = QLineEdit('')
        scoreLabel = QLabel('Score:')
        scoreLine = QLineEdit('')
        hbox1.addWidget(nameLabel)
        hbox1.addWidget(nameLine)
        hbox1.addWidget(ageLabel)
        hbox1.addWidget(ageLine)
        hbox1.addWidget(scoreLabel)
        hbox1.addWidget(scoreLine)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        amountLabel = QLabel('Amount')
        amountLine = QLineEdit('')
        keyLabel = QLabel('Key')
        keyComboBox = QComboBox()
        hbox2.addWidget(amountLabel)
        hbox2.addWidget(amountLine)
        hbox2.addWidget(keyLabel)
        hbox2.addWidget(keyComboBox)

        hbox3 = QHBoxLayout()
        hbox3.addStretch(1)
        addButton = QPushButton('Add')
        delButton = QPushButton('Del')
        findButton = QPushButton('Find')
        incButton = QPushButton('Inc')
        showButton = QPushButton('show')
        hbox3.addWidget(addButton)
        hbox3.addWidget(delButton)
        hbox3.addWidget(findButton)
        hbox3.addWidget(incButton)
        hbox3.addWidget(showButton)

        hbox4 = QHBoxLayout()
        resultLabel = QLabel('Result:')
        hbox4.addWidget(resultLabel)

        hbox5 = QHBoxLayout()
        resultText = QTextEdit('')
        hbox5.addWidget(resultText)

        vbox = QVBoxLayout()
        vbox.addLayout(hbox1)
        vbox.addLayout(hbox2)
        vbox.addLayout(hbox3)
        vbox.addLayout(hbox4)
        vbox.addLayout(hbox5)

        self.setLayout(vbox)
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')
        self.show()

    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb =  pickle.load(fH)
        except:
            pass
        else:
            pass
        fH.close()


    # write the data into person db
    def writeScoreDB(self):
        fH = open(self.dbfilename, 'wb')
        pickle.dump(self.scoredb, fH)
        fH.close()

    def showScoreDB(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())