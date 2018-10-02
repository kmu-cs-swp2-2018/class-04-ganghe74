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
        self.nameLine = QLineEdit('')
        ageLabel = QLabel('Age:')
        self.ageLine = QLineEdit('')
        scoreLabel = QLabel('Score:')
        self.scoreLine = QLineEdit('')
        hbox1.addWidget(nameLabel)
        hbox1.addWidget(self.nameLine)
        hbox1.addWidget(ageLabel)
        hbox1.addWidget(self.ageLine)
        hbox1.addWidget(scoreLabel)
        hbox1.addWidget(self.scoreLine)

        hbox2 = QHBoxLayout()
        hbox2.addStretch(1)
        amountLabel = QLabel('Amount')
        self.amountLine = QLineEdit('')
        keyLabel = QLabel('Key')
        self.keyComboBox = QComboBox()
        self.keyComboBox.addItems(['Name', 'Age', 'Score'])
        hbox2.addWidget(amountLabel)
        hbox2.addWidget(self.amountLine)
        hbox2.addWidget(keyLabel)
        hbox2.addWidget(self.keyComboBox)

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
        addButton.clicked.connect(self.addScoreDB)
        delButton.clicked.connect(self.delScoreDB)
        findButton.clicked.connect(self.findScoreDB)
        incButton.clicked.connect(self.incScoreDB)
        showButton.clicked.connect(self.showScoreDB)

        hbox4 = QHBoxLayout()
        resultLabel = QLabel('Result:')
        hbox4.addWidget(resultLabel)

        hbox5 = QHBoxLayout()
        self.resultText = QTextEdit('')
        self.resultText.setReadOnly(True)
        hbox5.addWidget(self.resultText)

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
        self.resultText.clear()
        for p in sorted(self.scoredb, key=lambda person: person[self.keyComboBox.currentText()]):
            temp = ''
            for attr in sorted(p):
                temp += str(attr) + '=' + str(p[attr]) + '\t'
            self.resultText.append(temp)

    def addScoreDB(self):
        try:
            record = {'Name':self.nameLine.text(), 'Age':int(self.ageLine.text()), 'Score':int(self.scoreLine.text())}
        except ValueError as e:
            self.resultText.clear()
            self.resultText.append('Age or Score must be integer')
            return
        self.scoredb += [record]
        self.showScoreDB()

    def delScoreDB(self):
        for p in self.scoredb:
            if self.nameLine.text() == p['Name']:
                self.scoredb.remove(p)
        self.showScoreDB()

    def findScoreDB(self):
        self.resultText.clear()
        for p in self.scoredb:
            if p['Name'] == self.nameLine.text():
                temp = ''
                for attr in sorted(p):
                    temp += str(attr) + '=' + str(p[attr]) + '\t'
                self.resultText.append(temp)

    def incScoreDB(self):
        for p in self.scoredb:
            if p['Name'] == self.nameLine.text():
                p['Score'] += int(self.amountLine.text())
        self.showScoreDB()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())