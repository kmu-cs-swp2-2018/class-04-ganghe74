import pickle
import sys
from PyQt5.QtWidgets import (QWidget, QPushButton,
    QHBoxLayout, QVBoxLayout, QApplication, QLabel,
    QComboBox, QTextEdit, QLineEdit)
from PyQt5.QtCore import Qt


class ScoreDB(QWidget):

    def __init__(self):
        super().__init__()
        self.dbfilename = 'assignment6.dat'
        self.initUI()
        self.scoredb = []
        self.readScoreDB()
        self.showScoreDB()


    def initUI(self):
        self.setGeometry(300, 300, 500, 250)
        self.setWindowTitle('Assignment6')

        # 첫 번째 행 : label x 3 , LineEdit x 3
        self.nameLabel = QLabel("Name:")
        self.ageLabel = QLabel("Age:")
        self.scoreLabel = QLabel("Score:")

        self.line1_1 = QLineEdit()
        self.line1_2 = QLineEdit()
        self.line1_3 = QLineEdit()

        self.hbox1 = QHBoxLayout()
        self.hbox1.addWidget(self.nameLabel)
        self.hbox1.addWidget(self.line1_1)
        self.hbox1.addWidget(self.ageLabel)
        self.hbox1.addWidget(self.line1_2)
        self.hbox1.addWidget(self.scoreLabel)
        self.hbox1.addWidget(self.line1_3)

        #두 번째 행 : addStretch(1), Label x 2, LineEdit x 1, Combobox x 1
        self.amountLabel = QLabel("Amount:")
        self.keyLabel = QLabel("Key:")

        self.line2_1 = QLineEdit()
        self.cb = QComboBox()
        self.cb.addItems(["Name", "Age", "Score"])

        self.hbox2 = QHBoxLayout()
        self.hbox2.addStretch(1)
        self.hbox2.addWidget(self.amountLabel)
        self.hbox2.addWidget(self.line2_1)
        self.hbox2.addWidget(self.keyLabel)
        self.hbox2.addWidget(self.cb)

        # 세 번째 행: PushButton x 5

        self.addButton = QPushButton("Add")
        self.delButton = QPushButton("Del")
        self.findButton = QPushButton("Find")
        self.incButton = QPushButton("Inc")
        self.showButton = QPushButton("Show")

        self.hbox3 = QHBoxLayout()
        self.hbox3.addWidget(self.addButton)
        self.hbox3.addWidget(self.delButton)
        self.hbox3.addWidget(self.findButton)
        self.hbox3.addWidget(self.incButton)
        self.hbox3.addWidget(self.showButton)

        # 네 번째 행 : Label x 1

        self.resultLabel = QLabel("Result:")

        self.hbox4 = QHBoxLayout()
        self.hbox4.addWidget(self.resultLabel)

        # 다섯 번째 행 : TextEdit x 1

        self.text = QTextEdit()

        self.hbox5 = QHBoxLayout()
        self.hbox5.addWidget(self.text)

        # 각 행 순서대로 배치

        self.vbox = QVBoxLayout()
        self.vbox.addLayout(self.hbox1)
        self.vbox.addLayout(self.hbox2)
        self.vbox.addLayout(self.hbox3)
        self.vbox.addLayout(self.hbox4)
        self.vbox.addLayout(self.hbox5)

        self.setLayout(self.vbox)

        # UI 구현 끝.


        # 이벤트 핸들러

        self.addButton.clicked.connect(self.buttonClicked)
        self.delButton.clicked.connect(self.buttonClicked)
        self.findButton.clicked.connect(self.buttonClicked)
        self.incButton.clicked.connect(self.buttonClicked)
        self.showButton.clicked.connect(self.buttonClicked)

        self.show()

    def buttonClicked(self):
        sender = self.sender() # sender 설정
        name = self.line1_1.text()
        age = self.line1_2.text()
        score = self.line1_3.text()
        amount = self.line2_1.text()
        scdb = self.scoredb

        # 버튼이 클릭되었을 때 무슨 버튼 인지에 따라 실행문을 나눔
        if sender.text() == 'Add':
            if name != "" and age != "" and score != "":
                try:
                    record = {'Name': name, 'Age': int(age), 'Score': int(score)}
                    scdb += [record]
                    self.text.setText(str(scdb))
                except:
                    self.text.setText("Try Again!")
            else: self.text.setText("Try Again!")
        elif sender.text() == 'Del':
            if name != "":
                try:
                    for i in scdb:
                        if i['Name'] == name:
                            scdb.remove(i)
                    self.text.setText(str(scdb))
                except:
                    self.text.setText("Try Again!")

        elif sender.text() == 'Find':
            if name != "":
                try:
                    findList = []
                    for j in scdb:
                        if j['Name'] == name:
                            findList += [j]
                    self.text.setText(str(findList))
                except:
                    self.text.setText("Try Again!")

        elif sender.text() == "Inc":
            if name != '' and amount != '':
                try:
                    for k in scdb:
                        if k['Name'] == name:
                            k['Score'] = k.get('Score') + int(amount)
                    self.text.setText(str(scdb))
                except:
                    self.text.setText("Try Again!")
        elif sender.text() == "Show":
            try:
                keyname = self.cb.currentText()
                sortedscdb = sorted(scdb, key=lambda person: person[keyname])
                self.text.setText(str(sortedscdb))
            except:
                self.text.setText("Try Again!")


    def closeEvent(self, event):
        self.writeScoreDB()

    def readScoreDB(self):
        try:
            fH = open(self.dbfilename, 'rb')
        except FileNotFoundError as e:
            self.scoredb = []
            return

        try:
            self.scoredb = pickle.load(fH)
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
        sortedscoredb = sorted(self.scoredb, key=lambda person:person['Name'])
        self.text.setText(str(sortedscoredb))



if __name__ == '__main__':    
    app = QApplication(sys.argv)
    ex = ScoreDB()
    sys.exit(app.exec_())