import sys
from PyQt5.QtWidgets import *
app = QApplication(sys.argv)
print(sys.argv)
label = QPushButton("Quit")
label.show()
app.exec_()