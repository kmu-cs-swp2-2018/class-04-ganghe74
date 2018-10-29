from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLayout, QGridLayout

from keypad import numPadList, operatorList
from functions import functionMap, functionList
from constants import constantMap, constantList
from Button import Button
from incontinuous import incontinuousList

class Calculator(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)

        # Display Window
        self.display = QLineEdit()
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.display.setMaxLength(40)

        # Button Creation and Placement
        numLayout = QGridLayout()
        opLayout = QGridLayout()
        constLayout = QGridLayout()
        funcLayout = QGridLayout()

        buttonGroups = {
            'num': {'buttons': numPadList, 'layout': numLayout, 'columns': 3},
            'op': {'buttons': operatorList, 'layout': opLayout, 'columns': 2},
            'constants': {'buttons': constantList, 'layout': constLayout, 'columns': 1},
            'functions': {'buttons': functionList, 'layout': funcLayout, 'columns': 1},
        }

        for label in buttonGroups.keys():
            r = 0; c = 0
            buttonPad = buttonGroups[label]
            for btnText in buttonPad['buttons']:
                button = Button(btnText, self.buttonClicked)
                buttonPad['layout'].addWidget(button, r, c)
                c += 1
                if c >= buttonPad['columns']:
                    c = 0; r += 1

        # Layout
        mainLayout = QGridLayout()
        mainLayout.setSizeConstraint(QLayout.SetFixedSize)

        mainLayout.addWidget(self.display, 0, 0, 1, 2)
        mainLayout.addLayout(numLayout, 1, 0)
        mainLayout.addLayout(opLayout, 1, 1)
        mainLayout.addLayout(constLayout, 2, 0)
        mainLayout.addLayout(funcLayout, 2, 1)

        self.setLayout(mainLayout)

        self.setWindowTitle("My Calculator")

        self.delLast = False


    def buttonClicked(self):

        if self.display.text() == 'Error!':
            self.display.setText('')

        button = self.sender()
        key = button.text()

        if key == '=':
            try:
                result = str(eval(self.display.text()))
            except:
                result = 'Error!'
            self.display.setText(result)
        elif key == 'C':
            self.display.clear()
        elif key == '←':
            self.display.setText(self.display.text()[:-1])
            self.delLast = False
        elif key in constantList:
            self.display.setText(self.display.text() + constantMap[constantList.index(key)][1])
        elif key in functionList:
            n = self.display.text()
            value = functionMap[functionList.index(key)][1](n)
            self.display.setText(str(value))
        elif key in incontinuousList:
            if not self.display.text()[-1:] in incontinuousList:
                self.display.setText(self.display.text() + key)
        elif key == '0':
            text = self.display.text()[-2:]
            if text[:1] in operatorList and text[1:] == '0':
                self.delLast = True
                return
            elif text[:1] == '0' and text[1:] == '':
                self.delLast = True
                return
            else:
                self.display.setText(self.display.text() + key)
        elif self.delLast:
            self.display.setText(self.display.text()[:-1] + key)
            self.delLast = False
        else:
            self.display.setText(self.display.text() + key)

    def keyPressEvent(self,e):
        if e.key()==Qt.Key_Escape:
            self.close()

if __name__ == '__main__':

    import sys

    app = QApplication(sys.argv)
    calc = Calculator()
    calc.show()
    sys.exit(app.exec_())